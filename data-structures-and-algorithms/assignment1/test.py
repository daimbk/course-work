import copy

class Spreadsheet:
    def __init__(self):
        self.sheet = None  # 2D array of values
        self.rows = 0
        self.cols = 0
        self.cursor = [0, 0]  # cursor's current position
        self.selection = [None, None, None, None]
        self.stack = []
        self.redo_stack = []

    def CreateSheet(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.sheet = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def Goto(self, row, col):
        self.cursor = [row, col]

    def Insert(self, val):
        if len(self.stack) == 0 or self.sheet != self.stack[-1]:
            self.stack.append(copy.deepcopy(self.sheet))
            self.sheet[self.cursor[0]][self.cursor[1]] = val
            self.stack.append(copy.deepcopy(self.sheet))
        else:
            self.sheet[self.cursor[0]][self.cursor[1]] = val
            self.stack.append(copy.deepcopy(self.sheet))

    def Select(self, row, col):
        self.selection = [self.cursor[0], self.cursor[1], row, col]

    def PrintSheet(self):
        for i in range(self.rows):
            print("".join(str(self.sheet[i][j]) + '\t\t' for j in range(self.cols)))

    def Undo(self):
        self.redo_stack.append(self.stack.pop())
        self.sheet = self.stack[-1]

    def Redo(self):
        self.stack.append(self.redo_stack.pop())
        self.sheet = self.stack[-1]


def main():
    sheet = Spreadsheet()

    sheet.CreateSheet(5, 5)
    sheet.Goto(3, 3)
    sheet.Insert(55)
    sheet.Goto(2, 2)
    sheet.Insert(69)
    sheet.PrintSheet()
    print()
    sheet.Undo()
    sheet.PrintSheet()
    print()
    sheet.Undo()
    sheet.PrintSheet()


main()
