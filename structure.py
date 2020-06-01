import numpy as np
from modules import *
from modules import control

board, npboard = board_stuff.get_board()
solved_board = solver.solve_it(board)

for i in board:
    print(i)