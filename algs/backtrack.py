import curses
from structs.cell import Cell
from structs.sudoku import Sudoku

class Backtracker(object):

    def __init__(self, sudoku, stdscr=None):
        # holds unsolved cells
        self.cells = []
        # tracks cell that is currently being solved
        self.curr_cell = 0
        # holds sudoku object to be solved
        self.sudoku = sudoku
        # holds size of the sudoku board
        self.board_size = sudoku.board_size
        # holds output dest of curses
        self.stdscr = stdscr
        # True if solved, False otherwise
        self.has_solution = False
        # iterate through puzzle and create cells for all unknowns
        for row in range(self.board_size):
            for col in range(self.board_size):
                # if value is zero it is unknown
                if self.sudoku.board[row][col] == 0:
                    # append cells in order of discovery (left - right) (top - bottom)
                    self.cells.append(Cell(sudoku, row, col, 0))

    def solve(self):
        '''solve the sudoku using the backtracking algorithm and display progress'''
        # while we still have work to do
        while not self.solved():
            # if we want to display progress
            if self.stdscr != None:
                # print the board
                self.sudoku.print_board(self.stdscr)
            # do next step and check if there is a solution
            if self.next_step() == False:
                break
        if self.solved():
            self.sudoku.print_puzzle(self.stdscr)
            self.sudoku.print_board(self.stdscr)
            self.stdscr.addstr(self.board_size + 1, 0, 'Successfully solved the puzzle! :)')
            self.stdscr.addstr(self.board_size + 2, 0, 'Press \'q\' to exit...')
            while True:
                c = self.stdscr.getch()
                if c == ord('q'):
                    break

    def next_step(self):
        '''performs the next step of the backtracking algorithm'''
        # increment the current cell num by 1
        self.cells[self.curr_cell].num += 1

        # check if a solution exists
        if self.no_solution():
            return False

        # check if the number in the cell is greater than the largest number allowed in the puzzle
        if self.cells[self.curr_cell].num > self.board_size:
            self.step_back()
        # check if the number in the cell is legal in the current state of the puzzle
        elif self.cells[self.curr_cell].is_legal():
            self.step_fwd()

    def step_fwd(self):
        '''advance to the next unsolved cell'''
        # update index on board with current num
        self.sudoku.update(self.cells[self.curr_cell])
        # move to next unsolved cell
        self.curr_cell += 1

    def step_back(self):
        '''backtrack one cell'''
        # reset cell to default (0)
        self.cells[self.curr_cell].num = 0
        # reset index on board (0)
        self.sudoku.update(self.cells[self.curr_cell])
        # move to previous unsolved cell
        self.curr_cell -= 1

    def solved(self):
        '''check if all unknowns have been solved'''
        # if current cell equals number of cells to solve then we have solved all unknowns
        self.has_solution = self.curr_cell == len(self.cells)
        return self.has_solution

    def no_solution(self):
        '''check if there is no valid solution'''
        # if current cell is negative we have no valid final board state
        if self.curr_cell < 0:
            return True
        return False
