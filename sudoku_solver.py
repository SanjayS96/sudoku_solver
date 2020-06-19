import numpy as np
from modules import *

title_screen = '''
   ███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗
   ██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║
   ███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║
   ╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║
   ███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝
   ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
'''

if __name__ == "__main__":
    print(title_screen)
    print('   Press enter to begin...', end='')
    input()
    board_data.save()
    board, npboard = board_data.get_board()
    solved_board = solver.solve_it(board)
    solved_npboard = np.asarray(board)
    changes_board = solved_npboard - npboard
    control.controller(changes_board)
