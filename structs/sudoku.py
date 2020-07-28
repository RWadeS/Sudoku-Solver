import structs.cell

class Sudoku(object):


    def __init__(self, puzzle, board_size=9, square_size=3):
        '''
        constructor for sudoku puzzle
        - assumes a 9x9 puzzle unless otherwise stated
        - tracks board size and square size (should solve puzzles of varying sizes)
        - saves the original puzzle to enable board reset
        '''
        self.puzzle = puzzle
        self.board_size = board_size
        self.square_size = square_size
        self.has_solution = None
        self.board = None

        # set up board for the first time
        self.fresh_start()

    def fresh_start(self):
        '''function used to reset the puzzle to be solved again'''
        self.board = []
        for row in self.puzzle:
            self.board.append(row.copy())

    def update(self, cell):
        '''updates the number on the board using the given cell'''
        self.board[cell.row][cell.col] = cell.num

    def print_puzzle(self, stdscr=None):
        '''prints the board to stdscr'''
        # if no arguments given print to stdout
        if stdscr == None:
            for row in self.board:
                print(row)
        #argument was given so try printing to curses and print to stdout if that fails
        else:
            try:
                for row in range(self.board_size):
                    stdscr.addstr(row, 0, '|' + '|'.join(str(s) for s in self.puzzle[row]) + '|')
                stdscr.refresh()
            except:
                for row in self.board:
                    print(row)

    def print_board(self, stdscr=None):
        '''prints the board to stdscr'''
        # if no arguments given print to stdout
        if stdscr == None:
            for row in self.board:
                print(row)
        #argument was given so try printing to curses and print to stdout if that fails
        else:
            try:
                for row in range(self.board_size):
                    stdscr.addstr(row, (self.board_size) * 3, '|' + '|'.join(str(s) for s in self.board[row]) + '|')
                stdscr.refresh()
            except:
                for row in self.board:
                    print(row)
