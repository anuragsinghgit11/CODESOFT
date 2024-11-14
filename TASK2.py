#TASK 2
#TIC-TAC-TOE AI
#Implement an AI agent that plays the classic game of Tic-Tac-Toe
#against a human player. You can use algorithms like Minimax with
#or without Alpha-Beta Pruning to make the AI player unbeatable.

algorithms.
import tkinter as tk
import numpy as np
import random

# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("600x700")
        self.master.configure(bg='black')
        
        self.header = tk.Label(self.master, text="TIC TAC TOE", font=('Arial', 36, 'bold'), bg='black', fg='white')
        self.header.pack(pady=20)

        # Create a frame for the game board to use grid layout
        self.board_frame = tk.Frame(self.master, bg='black')
        self.board_frame.pack(pady=10)

        self.board = np.full((3, 3), EMPTY)
        self.current_player = PLAYER_X
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        
        self.status_label = tk.Label(self.master, text="Player X's turn", font=('Arial', 20), bg='black', fg='white')
        self.status_label.pack(pady=10)

        # Retry button (hidden initially)
        self.retry_button = tk.Button(self.master, text='Try Again', font=('Arial', 20), command=self.reset_game, bg='lightgrey')
        self.retry_button.pack(pady=20)
        self.retry_button.pack_forget()  # Hide the retry button initially

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.board_frame, text='', font=('Arial', 36, 'bold'), width=5, height=2,
                                   command=lambda row=i, col=j: self.player_move(row, col), bg='grey', activebackground='lightgrey')
                button.grid(row=i, column=j, padx=10, pady=10)
                self.buttons[i][j] = button

    def player_move(self, row, col):
        if self.board[row, col] == EMPTY:
            self.make_move(row, col)
            if not self.check_winner():
                self.current_player = PLAYER_O
                self.status_label.config(text="Player O's turn")
                self.master.after(1000, self.ai_move)  # AI responds after 1 second

    def make_move(self, row, col):
        self.board[row, col] = self.current_player
        color = 'red' if self.current_player == PLAYER_X else 'green'
        self.buttons[row][col].config(text=self.current_player, fg=color)
        self.animate_move(row, col)

    def animate_move(self, row, col):
        self.buttons[row][col].config(bg='lightblue')
        self.master.after(200, lambda: self.buttons[row][col].config(bg='grey'))

    def check_winner(self):
        if self.is_winner(PLAYER_X):
            self.end_game("Player X Wins!")
            return True
        if self.is_winner(PLAYER_O):
            self.end_game("Player O Wins!")
            return True
        if self.is_draw():
            self.end_game("It's a Draw!")
            return True
        return False

    def end_game(self, message):
        self.status_label.config(text=message)
        for row in self.buttons:
            for button in row:
                button.config(state='disabled', bg='grey')
        self.retry_button.pack()  # Show the retry button

    def reset_game(self):
        self.board = np.full((3, 3), EMPTY)
        self.current_player = PLAYER_X
        self.status_label.config(text="Player X's turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal', bg='grey', fg='black')
        self.retry_button.pack_forget()  # Hide the retry button again

    def is_winner(self, player):
        return any(np.all(self.board[i, :] == player) for i in range(3)) or \
               any(np.all(self.board[:, j] == player) for j in range(3)) or \
               np.all(np.diag(self.board) == player) or \
               np.all(np.diag(np.fliplr(self.board)) == player)

    def is_draw(self):
        return np.all(self.board != EMPTY)

    def ai_move(self):
        if self.check_winner():  # Prevent AI from moving if the game is already won or drawn
            return
        
        available_moves = self.get_available_moves()
        if available_moves:
            row, col = random.choice(available_moves)  # Random move for simplicity
            self.make_move(row, col)
            if not self.check_winner():
                self.current_player = PLAYER_X
                self.status_label.config(text="Player X's turn")

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == EMPTY]

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
   
