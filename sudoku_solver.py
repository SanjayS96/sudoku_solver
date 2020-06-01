import numpy as np
from modules import *
from modules import control

if __name__ == "__main__":
    board_stuff.save()
    board, npboard = board_stuff.get_board()
    solved_board = solver.solve_it(board)
    solved_npboard = np.asarray(board)
    changes_board = solved_npboard - npboard
    control.controller(changes_board)