import win32api, win32con
import numpy as np
import keyboard
import time

def controller(c_board):

    def click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 948,372)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 948,372)
    
    mouse_x = np.array([390, 445, 500, 555, 610, 665, 720, 775, 830])
    mouse_y = np.array([266, 321, 376, 431, 486, 541, 596, 651, 706])
    
    nonzero_y, nonzero_x = np.nonzero(c_board)
    time.sleep(0.5)
    
    for i in range(len(nonzero_y)):
        x = nonzero_x[i]
        y = nonzero_y[i]
        
        time.sleep(0.1)
        win32api.SetCursorPos((mouse_x[x],mouse_y[y]))
        time.sleep(0.1)
        click()

        answer = c_board[y][x]
        answer = str(answer)
        keyboard.press_and_release(answer)  