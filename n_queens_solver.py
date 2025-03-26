import tkinter as tk
from tkinter import messagebox

class NQueensGame:
    def __init__(self, board_size):
        # Preparing the environment
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)] # Build 2D matrix with n rows and c columns
        self.root = tk.Tk() # Creates the main window
        self.root.title("N-Queens Game") # Title of the window
        self.canvas = tk.Canvas(self.root, width=board_size*50, height=board_size*50, bg="black") # Gives the main window the ability to have shapes and text within it
        self.canvas.pack()
        # Begin solving the game
        self.solve()

    def solve(self):
        if self._solve_dfs(0): # Enters dfs function first 
            self.create_board()
            messagebox.showinfo(title="Solution Found!", message=f'You Won!')
        else:
            messagebox.showerror(title="No solution Found!", message=f'Please try another NxN board')

    def _solve_dfs(self, col):
        # Prevents the function from calling itself again when col == board size
        if col == self.board_size:
            return True

        for row in range(self.board_size):
            if self.is_safe(row, col):
                # If the selected cell is safe make its value = 1 and move to the next cell in the same row
                self.board[row][col] = 1
                # The function calls itself recursively with increasing col value until reaching the board size to check all cells in the same row
                if self._solve_dfs(col + 1):
                    return True
                self.board[row][col] = 0

        return False

    def is_safe(self, row, col):
        # Check column
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.board_size, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def create_board(self):
        # 2 for loops to iterate through rows and columns
        for i in range(self.board_size):
            for j in range(self.board_size):
                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill=color)
                if self.board[i][j] == 1:
                    text_color = "black" if color == "white" else "white"
                    self.canvas.create_text(j*50+25, i*50+25, text="Q", fill=text_color, font=('Helvetica', 14))

        self.root.mainloop()

n = 8
game = NQueensGame(n)
