import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = []
        self.current_player = "X"
        self.board = [""] * 16  # Adjust the board size here (e.g., 4x4)

        # Create buttons and grid (same as before)
        for i in range(16):
            button = tk.Button(self.root, text="", font=("Helvetica", 24), height=2, width=5,
                               command=lambda i=i: self.clicked(i))
            button.grid(row=i // 4, column=i % 4)
            self.buttons.append(button)

        # Add a Reset button
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, bg="orange", fg="black")
        reset_button.grid(row=4, column=0, padx=10, pady=10)

        # Add an Exit button
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_game, bg="orange", fg="black")
        exit_button.grid(row=4, column=1, padx=10, pady=10)

        # Add a turn label
        self.turn_label = tk.Label(self.root, text=f"Turn: {self.current_player}", font=("Helvetica", 12))
        self.turn_label.grid(row=5, columnspan=4)

        # Initialize the timer
        self.timer_time = 0
        self.timer_label = tk.Label(self.root, text="Time: 0 seconds", font=("Helvetica", 12))
        self.timer_label.grid(row=6, columnspan=4)

        # Start the timer
        self.update_timer()

    def clicked(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Turn: {self.current_player}")

    def check_winner(self):
       # Check rows
        for row in range(0, 16, 4):
         if self.board[row] == self.board[row + 1] == self.board[row + 2] == self.board[row + 3] != "":
            return True

    # Check columns
        for col in range(4):
         if self.board[col] == self.board[col + 4] == self.board[col + 8] == self.board[col + 12] != "":
            return True

    # Check diagonals
         if self.board[0] == self.board[5] == self.board[10] == self.board[15] != "":
           return True
         if self.board[3] == self.board[6] == self.board[9] == self.board[12] != "":
           return True

        return False
    
    
    def reset_game(self):
        # Clear the board and reset the game
        for button in self.buttons:
            button.config(text="")
        self.board = [""] * 16
        self.current_player = "X"
        self.turn_label.config(text=f"Turn: {self.current_player}")
        self.timer_time = 0

    def exit_game(self):
        self.root.destroy()

    def update_timer(self):
        self.timer_time += 1
        self.timer_label.config(text=f"Time: {self.timer_time} seconds")
        self.root.after(1000, self.update_timer)  # Update every 1000ms (1 second)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()