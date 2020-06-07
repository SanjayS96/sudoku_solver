# Sanjay's Sudoku Solver
A basic interactive backtracking sudoku solver written in Python.  

## Features
  - Interact with web-based sudoku puzzles through emulating mouse and keyboard movements
  - Generate unique sudoku puzzles without using seed data
 
### Requirements
  - Keyboard
  ```pip install keyboard```
  - Pywin32
  ```pip install pywin32```
  - Numpy 
  ```pip install numpy```

### Requirements
This program requires pywin32, keyboard, and numpy:
```sh
pip install pywin32
pip install keyboard
pip install numpy
```

### Known Bugs 
  - This solver was built in Python 3.7 and has not been tested for Python 2.x
  - The generator module occasionally produces 'dumb' Sudokus. For more information,
  read my long-winded explanation below*

    A well-formed Suduko should only possess one solution; a sudoku that can only be 
    solved one way can be solved using logic as opposed to having to guess values for
    blank spaces. 
    
    One easy fix would be to have my solver module count the solutions it found.
    However, due to the nature of a recursive backtracking algorithm, implementing 
    a method to find all possible solutions would require a complete redesign of
    my algorithm.

### Planned Features   



License
----

MIT
