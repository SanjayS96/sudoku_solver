import numpy as np
from modules import *
from modules import control

<<<<<<< HEAD
board_stuff.save()
board, npboard = board_stuff.get_board()
solved_board = solver.solve_it(board)
solved_npboard = np.asarray(board)
changes_board = solved_npboard - npboard
control.controller(changes_board)
=======
if __name__ == "__main__":
    board_stuff.save()
    board, npboard = board_stuff.get_board()
    solved_board = solver.solve_it(board)
    solved_npboard = np.asarray(board)
    changes_board = solved_npboard - npboard
    control.controller(changes_board)
>>>>>>> 6c476e2222bf6d8423f00ed835575a97ce49bf46
