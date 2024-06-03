import tkinter as tk
from tkinter import messagebox
from multiprocessing import Pool, cpu_count


class SOS:
    def __init__(self, size=8):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'Player 1'
        self.current_letter = 'S'

    def enterChar(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_letter
            return True
        return False

    def switchPlayer(self):
        if self.current_player == 'Player 1':
            self.current_player = 'Player 2'
        else:
            self.current_player = 'Player 1'

    def changeChar(self, letter):
        self.current_letter = letter

    # to check if game has come to a draw
    def isBoardFull(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


def checkWinConditions(board, start_row, end_row, start_col, end_col):
    sosTrue = 0
    rows, cols = len(board), len(board[0])

    # win condition in rows eg. S | O | S
    for i in range(start_row, end_row):
        for j in range(max(0, start_col - 2), min(cols - 2, end_col)):
            if board[i][j:j + 3] == ['S', 'O', 'S']:
                sosTrue += 1

    # win condition in cols (vertical)
    for j in range(start_col, end_col):
        for i in range(max(0, start_row - 2), min(rows - 2, end_row)):
            if [board[i+k][j] for k in range(3)] == ['S', 'O', 'S']:
                sosTrue += 1

    # win condition diagonally in either direction
    for i in range(max(0, start_row - 2), min(rows - 2, end_row)):
        for j in range(max(0, start_col - 2), min(cols - 2, end_col)):
            if (board[i][j] == 'S' and board[i + 1][j + 1] == 'O' and board[i + 2][j + 2] == 'S'):
                sosTrue += 1
            if (board[i][j + 2] == 'S' and board[i + 1][j + 1] == 'O' and board[i + 2][j] == 'S'):
                sosTrue += 1

    return sosTrue


def checkWinRange(args):
    board, start_row, end_row, size = args
    return checkWinConditions(board, start_row, end_row, 0, size)


def parallelCheckWinConditions(board, size, num_processes=cpu_count()):
    pool = Pool(num_processes)
    rows_per_process = size // num_processes
    ranges = [(board, i * rows_per_process, (i + 1) * rows_per_process, size)
              for i in range(num_processes)]
    # ensure the last range includes any remaining rows
    ranges[-1] = (board, ranges[-1][1], size, size)
    results = pool.map(checkWinRange, ranges)
    pool.close()
    pool.join()
    return sum(results)


class GUI:
    def __init__(self, master):
        self.master = master
        self.game = SOS()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.gui()

    def gui(self):
        self.master.title("SOS")

        for i in range(8):
            for j in range(8):
                button = tk.Button(self.master, text=' ', width=4, height=2,
                                   command=lambda row=i, col=j: self.onClick(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.label = tk.Label(self.master, text="Current Player: Player 1")
        self.label.grid(row=8, columnspan=8)

        self.button_s = tk.Button(
            self.master, text='S', width=4, height=2, command=self.setS)
        self.button_s.grid(row=9, column=3)

        self.button_o = tk.Button(
            self.master, text='O', width=4, height=2, command=self.setO)
        self.button_o.grid(row=9, column=4)

    def setS(self):
        self.game.changeChar('S')

    def setO(self):
        self.game.changeChar('O')

    def onClick(self, row, col):
        if self.game.enterChar(row, col):
            self.buttons[row][col].config(text=self.game.current_letter)
            if parallelCheckWinConditions(self.game.board, 8) > 0:
                messagebox.showinfo(
                    "Game Over", f"{self.game.current_player} wins!")
                self.reset()
            elif self.game.isBoardFull():
                messagebox.showinfo("Game Over", "Draw!")
                self.reset()
            else:
                self.game.switchPlayer()
                self.label.config(
                    text=f"Current Player: {self.game.current_player}")
        else:
            messagebox.showwarning("Illegal", "No Cell Takeovers!")

    def reset(self):
        self.game = SOS()
        for i in range(8):
            for j in range(8):
                self.buttons[i][j].config(text=' ')
        self.label.config(text="Current Player: Player 1")


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
