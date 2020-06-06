import random
import numpy as np
from modules import solver

def make_random():
    np_z_board = np.zeros([9,9], int)
    z_board = np_z_board.tolist()
    
    digits = [1,2,3,4,5,6,7,8,9]

    for i in range(0,9,3):
        for j in range(0,9,3):
            
            x = random.randint(i,i+2)
            y = random.randint(j,j+2)
            
            z_board[x][y] = digits.pop(random.randint(0,len(digits)-1))

    solved = solver.solve_it(z_board)

    for i in range(9):
        for j in range(9):
            a = random.randint(0,1)

            if a != 0:
                solved[i][j] = 0 
    
    return solved

rando_board = make_random()