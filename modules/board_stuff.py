from bs4 import BeautifulSoup
import numpy as np
import keyboard
import time

def save():
    # keyboard.press_and_release('alt+tab')
    # time.sleep(0.3)
    # keyboard.press_and_release('ctrl+s')
    # time.sleep(0.3)
    # keyboard.write('board.html')
    # time.sleep(0.3)
    # keyboard.press_and_release('enter')
    # time.sleep(0.3)
    # keyboard.press_and_release('left')
    # time.sleep(0.3)
    # keyboard.press_and_release('enter')
    print('saved')
    time.sleep(1)

def get_board():
    ##Fetch board(list of lists) from soduko.com html file
    html_doc = 'C:\\Users\\Sanjay\\sudoku_solver\\boards\\board.html'

    with open(html_doc, 'rb') as fp:
        soup = BeautifulSoup(fp, from_encoding='UTF-8', features='html.parser')

    values = [
            'M8.954', 'M.12', 'M6.698', 'M15.855', 'M10.553 30.615c', 
            'M10.964', 'M3.017', 'M10.533 31.615c', 'M10.897'
    ]

    table = soup.findAll(class_='cell-value')
    board = []
    for cell in table:
        active_cell = cell.find('path')
        if active_cell == None:
            cell = 0
            board.append(cell)
        else:
            for n, v in enumerate(values, start=1):
                cell = active_cell['d']
                if v in cell:
                    cell = n
                    board.append(cell)

    board = np.asarray(board)
    board = board.reshape(9,9)
    npboard = board.reshape(9,9)
    board = board.tolist()

    return board, npboard