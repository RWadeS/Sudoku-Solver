from structs.sudoku import Sudoku
from algs.backtrack import Backtracker

import curses

def unit_test():
    # link to puzzle: https://www.websudoku.com/?level=1&set_id=5316832410
    puzzle =[[0, 9, 0, 0, 0, 3, 5, 0, 0],
    [1, 6, 7, 5, 2, 0, 0, 0, 4],
    [5, 0, 0, 0, 9, 0, 0, 0, 0],
    [0, 0, 8, 6, 0, 0, 3, 2, 5],
    [0, 0, 5, 0, 0, 0, 4, 0, 0],
    [4, 3, 9, 0, 0, 2, 8, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 3],
    [3, 0, 0, 0, 6, 4, 1, 7, 9],
    [0, 0, 1, 2, 0, 0, 0, 4, 0]]

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        sudoku = Sudoku(puzzle)
        backtracker = Backtracker(sudoku, stdscr)
        backtracker.solve()
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()

if __name__ == '__main__':
    unit_test()
