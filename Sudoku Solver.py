from pandas import np


class board:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def getpuzzle(self):
        return self.puzzle

    def print(self):
        for i in range(0,9):
            print(self.puzzle[i])

    def getnumber(self, xco, y):
        return cell(self.puzzle, xco, y)

    def getrow(self, rownum):
        return self.puzzle[int(rownum)]

    def getcolumn(self, colnum):
        return [row[colnum] for row in self.puzzle]

    def setnumber(self, newnumber, xco, y):
        self.puzzle[xco][y] = newnumber

    def noallocation(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.puzzle[i][j] == 0:
                    return cell(self.puzzle, i, j)
        return False

    def getblock(self, xco, y):
        last = np.zeros((3, 3))
        if xco <= 2:
            if y <= 2:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i)[j]
                return last
            elif 2 < y <= 5:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i)[j + 3]
                return last
            elif 5 < y <= 8:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i)[j + 6]
                return last
        elif 2 < xco <= 5:
            if y <= 2:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i + 3)[j]
                return last
            elif 2 < y <= 5:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i + 3)[j + 3]
                return last
            elif 5 < y <= 8:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i + 3)[j + 6]
                return last
        elif 5 < xco <= 8:
            if y <= 2:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i + 6)[j]
                return last
            elif 2 < y <= 5:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i + 6)[j + 3]
                return last
            elif 5 < y <= 8:
                for i in range(0, 3):
                    for j in range(0, 3):
                        last[i, j] = self.getrow(i + 6)[j + 6]
                return last


class cell(board):

    def __init__(self, puzzle, xco, yco):
        self.puzzle = puzzle
        self.x = xco
        self.y = yco

    def isvalid(self,number):
        count1 = 0
        count2 = 0
        count3 = 0
        for i in range(0, 9):
            if self.getrow(self.x)[i] == number:
                count1 += 1
            if self.getcolumn(self.y)[i] == number:
                count2 += 1
        for i in range(0, 3):
            for j in range(0, 3):
                if self.getblock(self.x, self.y)[i][j] == number:
                    count3 += 1

        if count1 >= 1 or count2 >= 1 or count3 >= 1:
            return False
        else:
            return True

    def getx(self):
        return self.x

    def gety(self):
        return self.y


x = [[0, 0, 0, 0, 4, 0, 8, 0, 0],
     [8, 0, 0, 0, 3, 9, 0, 0, 0],
     [5, 6, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 8, 0, 0, 5, 0, 0, 6],
     [7, 2, 0, 0, 0, 0, 0, 9, 0],
     [0, 0, 0, 0, 0, 6, 7, 0, 3],
     [6, 0, 0, 0, 0, 0, 9, 8, 0],
     [0, 5, 9, 0, 0, 7, 0, 0, 4],
     [0, 0, 0, 0, 0, 1, 0, 3, 0]]


def sudoku_solver(puzzle):
    if puzzle.noallocation() != False:
        xco = puzzle.noallocation().getx()
        yco = puzzle.noallocation().gety()
    else:
        return True

    for i in range(1, 10):
        if puzzle.getnumber(xco, yco).isvalid(i):
            puzzle.setnumber(i, xco, yco)
            if sudoku_solver(puzzle):
                return True
            else:
                puzzle.setnumber(0, xco, yco)
    return False


a = board(x)
b = cell(x, 0, 1)

sudoku_solver(a)
a.print()