import tkinter as tk
from tkinter import messagebox

class NQueensGame:
    def __init__(self, master, board_size):
        # Constructor method to initialize the game
        self.master = master  # Tkinter root window
        self.board_size = board_size  # Size of the chessboard (board_size x board_size)
        self.board = [[0] * board_size for _ in range(board_size)]  # Initialize an empty board
        self.create_board()  # Create the graphical representation of the board

    def create_board(self):
        # Method to create the GUI representation of the game board
        self.buttons = [[None] * self.board_size for _ in range(self.board_size)]  # 2D list to store buttons
        
        # Loop through each row and column to create buttons for each square
        for i in range(self.board_size):
            for j in range(self.board_size):
                # Determine the color of the square based on its position (alternating black and white)
                color = "white" if (i + j) % 2 == 0 else "black"
                # Create a button with specified attributes and command (toggle_queen)
                self.buttons[i][j] = tk.Button(self.master, width=5, height=2, bg=color, font=('Helvetica', 14),
                                            command=lambda row=i, col=j: self.toggle_queen(row, col))
                # Place the button on the grid
                self.buttons[i][j].grid(row=i, column=j)

    def toggle_queen(self, row, col):
        # Method to toggle the presence of a queen at the specified position
        if self.board[row][col] == 1:
            self.remove_queen(row, col)  # If a queen is present, remove it
        else:
            self.place_queen(row, col)  # If no queen is present, place one

    def place_queen(self, row, col):
        # Method to place a queen at the specified position
        if self.is_safe(row, col):
            # If it's safe to place the queen (no conflicts), update the board
            self.board[row][col] = 1
            self.update_board()
        else:
            # If placing the queen causes conflicts, show an error message
            messagebox.showerror(title="Invalid move!", message=f'Queens can attack each other by this move!')

    def remove_queen(self, row, col):
        # Method to remove a queen from the specified position
        self.board[row][col] = 0  # Update the board to indicate the absence of a queen
        self.update_board()  # Update the GUI representation of the board

    def is_safe(self, row, col):
        # Method to check if it's safe to place a queen at the specified position
        # Check row and column for any existing queens
        for i in range(self.board_size):
            if self.board[i][col] == 1 or self.board[row][i] == 1:
                return False  # If a queen exists in the same row or column, it's not safe
        
        # Check diagonals for any existing queens
        for j in range(self.board_size - col):
            # Check the upper-left diagonal
            if (col - (row - j) >= 0 and self.board[j][col - (row - j)] == 1) or \
                    (col + (row - j) < self.board_size and self.board[j][col + (row - j)] == 1):
                return False  # If a queen exists in the diagonal, it's not safe

        return True  # If no conflicts are found, it's safe to place the queen

    def update_board(self):
        # Method to update the GUI representation of the board
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 1:
                    # If a queen is present at the position, update the button text and color
                    fg_color = "black" if (i + j) % 2 == 0 else "white"  # Invert the text color for visibility
                    self.buttons[i][j].config(text="Q", state=tk.NORMAL, foreground=fg_color)
                else:
                    # If no queen is present, reset the button text and state
                    self.buttons[i][j].config(text="", state=tk.NORMAL)

        # Check if the game is won (all queens are placed)
        self.active_queens = sum(row.count(1) for row in self.board)
        if self.active_queens == self.board_size:
            # If all queens are placed, show a victory message
            messagebox.showinfo(title="You Won!", message=f'You Won!')

def main():
    root = tk.Tk()  # Create Tkinter root window
    root.title("N-Queens Game")  # Set title of the window
    game = NQueensGame(root, board_size=8)  # Initialize NQueensGame instance with board size 8
    root.mainloop()  # Start Tkinter event loop

if __name__ == "__main__":
    main()
