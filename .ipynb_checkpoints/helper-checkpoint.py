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
    E.g: up <=> down

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
