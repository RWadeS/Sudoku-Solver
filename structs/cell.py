import structs.sudoku

class Cell(object):

    def __init__(self, sudoku, row, col, num):
        '''constructor for a Cell object
        - contains parent puzzle
        - tracks position of Cell in parent puzzle with row/col
        - tracks current number in cell
        '''
        # holds cells parent puzzle
        self.sudoku = sudoku
        # holds row position in parent puzzle
        self.row = row
        # holds column position in parent puzzle
        self.col = col
        # holds value in cell (unsolved = 0)
        self.num = num

    def get_row(self):
        '''returns a list of all numbers contained in the cells row'''
        return self.sudoku.board[self.row]

    def get_col(self):
        '''returns a list of all numbers contained in the cells col'''
        col = []
        for row in range(self.sudoku.board_size):
            col.append(self.sudoku.board[row][self.col])
        return col

    def get_square(self):
        '''returns a list of all numbers contained in the cells region'''
        region = []
        # save square size for ease of use and nicer code
        size = self.sudoku.square_size
        # calculate initial row (position of first row in the cells region)
        init_row = (self.row // size) * size
        init_col = (self.col // size) * size
        for row in range(init_row, init_row + size):
            for col in range(init_col, init_col + size):
                region.append(self.sudoku.board[row][col])
        return region

    def get_region(self):
        '''returns the set of all numbers in the cells area'''
        # aggregate all numbers from region, row, and column into one set
        nums = set()
        nums = nums.union(set(self.get_row()))
        nums = nums.union(set(self.get_col()))
        nums = nums.union(set(self.get_square()))
        return nums

    def is_legal(self):
        '''returns true if current number is valid in row/col/square'''
        # obtain set of all numbers in range of the cell
        nums = self.get_region()

        if self.num in nums:
            return False
        return True
