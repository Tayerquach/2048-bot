from random import random, randint
import constants as c
import numpy as np

def create_new_game(n):

    """
    Create new matrix

    :param n: Number of rows or cols (e.g n = 4 => 4 x 4)
    :return: A grid n x n
    """
    matrix = np.array([[0] * n for _ in range(n)])

    matrix = put_new_cell(matrix)
    matrix = put_new_cell(matrix)
    return np.array(matrix)

def put_new_cell(matrix):
    """
    Create a function to add 2 or 4

    :param matrix: Matrix needs to be add a value
    :return: A random matrix after adding a value
    """

    rows, cols = matrix.shape[0], matrix.shape[1]
    n = 0
    r = 0
    i_s=[0]*rows*cols
    j_s=[0]*cols*rows
    for i in range(rows):
        for j in range(cols):
            if not matrix[i,j]: #Check element equal to 0: grid[i,j] = 0
                i_s[n]=i
                j_s[n]=j
                n+=1
    if n > 0:
        r = randint(0, n-1) #Random position to add values 2 or 4
        matrix[i_s[r], j_s[r]] = 2 if random() < 0.9 else 4 #90% is 2 
    return matrix

def reverse(matrix):
    """
    Create a function to reverse matrix.
    E.g: left <=> right

    :param matrix: original matrix
    :return: reversed matrix
    """
    new = []
    rows, cols = matrix.shape[0], matrix.shape[1]
    for i in range(rows):
        new.append([])
        for j in range(cols-1, -1, -1): #Print reverse 3, 2, 1, 0
            new[i].append(matrix[i][j])
    return np.array(new)

def transpose(matrix):
    """
    Create a function to transpose matrix.
    E.g: rows <=> cols

    :param matrix: original matrix
    :return: transposed matrix
    """
    new = []
    rows, cols = matrix.shape[0], matrix.shape[1]
    for i in range(cols):
        new.append([])
        for j in range(rows):
            new[i].append(matrix[j][i])
    return np.array(new)

def cover_up(matrix):
    """
    Create a function to pull all values to the left side.
    E.g:   [[4 0 0 2]   <=>  [[4 2 0 0] 
            [0 0 0 0]         [0 0 0 0]
            [0 0 2 0]         [2 0 0 0]
            [0 8 2 0]]        [8 2 0 0]]

    :param matrix: original matrix
    :return: cover-up matrix and check the ability of moving elements to left.
    """
    n = len(matrix)
    new = [[0] * n for _ in range(n)]
    done = False
    for i in range(n):
        count = 0
        for j in range(n):
            if matrix[i][j] != 0:
                new[i][count] = matrix[i][j]
                if j != count:
                    done = True
                count += 1
    return np.array(new), done

def merge(matrix, done):
    """
    Create a function to add 2 next elements
    E.g:   [[2 2 0 0]   <=>  [[4 0 0 0] 
            [0 0 0 0]         [0 0 0 0]
            [0 0 2 0]         [0 0 2 0]
            [0 4 2 2]]        [0 4 4 0]]

    :param matrix: original matrix
    :return: cover-up matrix and check the ability of moving elements to left.
    """
    rows, cols = matrix.shape[0], matrix.shape[1]
    score = 0
    for i in range(rows):
        for j in range(cols - 1):
            if matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0:
                matrix[i][j] *= 2
                matrix[i][j+1] = 0
                score = matrix[i][j]
                done = True
                
    return matrix, done, score

def left(matrix):
    """
    Create a push_left function

    :param matrix: original matrix
    :return: 
    1) matrix after shifting left
    2) done: if done is False: the initial matrix cannot push left as well as merge => keep the matrix
    """
    # print("left")
    # return matrix after shifting left
    matrix, done = cover_up(matrix)
    matrix, done, score = merge(matrix, done)
    if done:
        matrix = cover_up(matrix)[0]
        matrix = put_new_cell(matrix)
    return matrix, done, score

def right(matrix):
    """
    Create a push_right function

    :param matrix: original matrix
    :return: 
    1) matrix after shifting right
    2) done: if done is False: the initial matrix cannot push right as well as merge => keep the matrix
    """
    # print("right")
    # return matrix after shifting right
    matrix = reverse(matrix) #covert right-hand elements into left-hand ones
    matrix, done = cover_up(matrix)
    matrix, done, score = merge(matrix, done)
    if done: 
        matrix = cover_up(matrix)[0]
        matrix = put_new_cell(matrix)
    matrix = reverse(matrix)
    return matrix, done, score

def up(matrix):
    """
    Create a push_up function

    :param matrix: original matrix
    :return: 
    1) matrix after push up
    2) done: if done is False: the initial matrix cannot push up as well as merge => keep the matrix
    """
    # print("up")
    # return matrix after shifting up
    matrix = transpose(matrix)
    matrix, done = cover_up(matrix)
    matrix, done, score = merge(matrix, done)
    if done:
        matrix = cover_up(matrix)[0]
        matrix = put_new_cell(matrix)
    matrix = transpose(matrix)
    return matrix, done, score

def down(matrix):
    """
    Create a push_down function

    :param matrix: original matrix
    :return: 
    1) matrix after push down
    2) done: if done is False: the initial matrix cannot push down as well as merge => keep the matrix
    """
    # print("down")
    matrix = reverse(transpose(matrix)) #up -> left, right(raw down) --> left
    matrix, done = cover_up(matrix)
    matrix, done, score = merge(matrix, done)
    if done:      
        matrix = cover_up(matrix)[0]
        matrix = put_new_cell(matrix)
    matrix = transpose(reverse(matrix))
    return matrix, done, score

def game_state(matrix):
    """
    Create a getting state function

    :param matrix: original matrix
    :return: state ["win", "not over", "lose"]
    """
    # check for win cell
    rows, cols = matrix.shape[0], matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 2048:
                return 'win'
    # check for any zero entries
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                return 'not over'
    # check for same cells that touch each other
    for i in range(rows - 1):
        # intentionally reduced to check the row on the right and below
        # more elegant to use exceptions but most likely this will be their solution
        for j in range(cols-1):
            if matrix[i][j] == matrix[i+1][j] or matrix[i][j+1] == matrix[i][j]:
                return 'not over'
    for k in range(cols-1):  # to check the left/right entries on the last row
        if matrix[rows - 1][k] == matrix[rows-1][k+1]:
            return 'not over'
    for j in range(rows-1):  # check up/down entries on last column
        if matrix[j][cols-1] == matrix[j+1][cols-1]:
            return 'not over'
    return 'lose'

def print_grid(matrix):
    """Print a pretty grid to the screen."""
    print("")
    wall = "+------"*matrix.shape[1]+"+"
    print(wall)
    for i in range(matrix.shape[0]):
        meat = "|".join("{:^6}".format(matrix[i,j]) for j in range(matrix.shape[1]))
        print("|{}|".format(meat))
        print(wall)

def arrayisin(array, list_of_arrays):
    for elements in list_of_arrays:
        if np.array_equal(array, elements):
            return True
    return False

def check_depth(frontiers, visited_states):
    flag = False
    for i in frontiers:
        if  (i == np.array(visited_states)).all():
            flag = True
            break
    return flag
