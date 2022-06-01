import numpy as np
from random import random, randint

class Function:
    def __init__(self, grid_array):
        self.grid = grid_array
        pass
        
    def print_grid(self):
        """Print a pretty grid to the screen."""
        print("")
        wall = "+------"*self.grid.shape[1]+"+"
        print(wall)
        for i in range(self.grid.shape[0]):
            meat = "|".join("{:^6}".format(self.grid[i,j]) for j in range(self.grid.shape[1]))
            print("|{}|".format(meat))
            print(wall)

    def stack(self):
        rows, cols = self.grid.shape[0], self.grid.shape[1]
        new_matrix = np.zeros(shape=(rows, cols), dtype='uint16')
        for i in range(rows):
            fill_position = 0
            for j in range(cols):
                if self.grid[i][j] != 0:
                    new_matrix[i][fill_position] = self.grid[i][j]
                    fill_position +=1
        self.grid = np.array(new_matrix)
        return self.grid

    def combine(self):
        score = 0
        moved = False
        rows, cols = self.grid.shape[0], self.grid.shape[1]
        for i in range(rows):
            for j in range(cols-1):
                if self.grid[i][j] != 0 and self.grid[i][j] == self.grid[i][j + 1]:
                    self.grid[i][j] *= 2
                    self.grid[i][j + 1] = 0
                    moved = True
                    score += self.grid[i][j]
        score = score if moved else -1

        return self.grid

    def reverse(self):
        new_matrix = []
        rows, cols = self.grid.shape[0], self.grid.shape[1]
        for i in range(rows):
            new_matrix.append([])
            for j in range(cols-1,-1,-1): #Print reverse 3, 2, 1, 0
                new_matrix[i].append(self.grid[i][j])
        self.grid = np.array(new_matrix)
        return self.grid

    def transpose(self):
        new_matrix = []
        rows, cols = self.grid.shape[0], self.grid.shape[1]
        for i in range(cols):
            new_matrix.append([])
            for j in range(rows):
                new_matrix[i].append(self.grid[j][i])
        
        self.grid = np.array(new_matrix)
        return self.grid

    def any_possible_moves(self):
        """Return True if there are any legal moves, and False otherwise."""
        rows, cols = self.grid.shape[0], self.grid.shape[1]
        for i in range(rows):
            for j in range(cols):
                e = self.grid[i, j]
                if not e: #e = 0
                    return True
                if j and e == self.grid[i, j-1]: #Check all elements in each ROW which has the same values
                    return True
                if i and e == self.grid[i-1, j]: #Check all elements in each COLUMN which has the same values
                    return True
        return False

    def put_new_cell(self):
        n = 0
        r = 0
        i_s=[0]*16
        j_s=[0]*16
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if not self.grid[i,j]: #Check element having 0: grid[i,j] = 0
                    i_s[n]=i
                    j_s[n]=j
                    n+=1
        if n > 0:
            r = randint(0, n-1)
            self.grid[i_s[r], j_s[r]] = 2 if random() < 0.9 else 4

        return n


    def prepare_next_turn(self):
        """
        Spawn a new number on the grid; then return the result of
        any_possible_moves after this change has been made.

        Return True or False
        * Check there is any 0 values in grid
        * Check any_possible_moves

        """
        empties = self.put_new_cell()    
        return empties>1 or self.any_possible_moves()