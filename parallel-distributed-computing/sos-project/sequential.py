import numpy as np
import tkinter as tk
from tkinter import messagebox


class SOS:
    def __init__(self, size=8):
        self.size = size
        self.board = np.full((size, size), ' ')
        self.current_player = 'Player 1'
        self.current_letter = 'S'

    def enterChar(self, row, col):
        if self.board[row, col] == ' ':
            self.board[row, col] = self.current_letter
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
        return not np.any(self.board == ' ')


def checkWinConditions(board):
    sosTrue = 0
    rows, cols = board.shape

    # win condition in rows eg. S | O | S
    for i in range(rows):
        for j in range(cols - 2):
            if np.array_equal(board[i, j:j+3], ['S', 'O', 'S']):
                sosTrue += 1

    # win condition in cols (vertical)
    for j in range(cols):
        for i in range(rows - 2):
            if np.array_equal(board[i:i+3, j], ['S', 'O', 'S']):
                sosTrue += 1

    # win condition diagonally in either direction
    for i in range(rows - 2):
        for j in range(cols - 2):
            if board[i, j] == 'S' and board[i+1, j+1] == 'O' and board[i+2, j+2] == 'S':
                sosTrue += 1

            if board[i, j+2] == 'S' and board[i+1, j+1] == 'O' and board[i+2, j] == 'S':
                sosTrue += 1

    return sosTrue


class GUI:
    def __init__(self, master):
        self.master = master
        self.game = SOS()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.gui()

    def gui(self):
        self.master.title("SOS Game")

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
            if checkWinConditions(self.game.board) > 0:
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
