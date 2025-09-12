import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    """
    Rock-Paper-Scissors Game
    ------------------------
    This class provides a simple, user-friendly GUI Rock-Paper-Scissors game 
    where you play against the computer. Your score and the computer's
    score are both tracked over multiple rounds.
    """

    def __init__(self, root):
        """
        Set up the application window and initialize game variables.
        """
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        # Scores tracking for user and computer
        self.user_score = 0
        self.computer_score = 0

        # Helpful instruction for the user
        tk.Label(root, text="Pick rock, paper, or scissors and click Play!", font=("Arial", 12)).pack(pady=10)

        # Frame to house choice buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        # Create choice buttons for Rock, Paper, and Scissors
        for choice in ["Rock", "Paper", "Scissors"]:
            tk.Button(button_frame, text=choice, width=11, command=lambda ch=choice: self.set_user_choice(ch)).pack(side=tk.LEFT, padx=4)

        # Store the current user's choice
        self.user_choice = None

        # Info labels showing choices and outcome
        self.user_choice_label = tk.Label(root, text="Your choice: None", font=("Arial", 10))
        self.user_choice_label.pack()
        self.computer_choice_label = tk.Label(root, text="Computer's choice: None", font=("Arial", 10))
        self.computer_choice_label.pack()
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=8)
        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 11))
        self.score_label.pack()

        # Play again and reset buttons
        tk.Button(root, text="Play", command=self.play_round).pack(pady=7)
        tk.Button(root, text="Reset Scores", command=self.reset_scores).pack(pady=3)

    def set_user_choice(self, choice):
        """
        Called whenever the user clicks a choice button.
        Updates the user_choice and refreshes label.
        """
        self.user_choice = choice
        self.user_choice_label.config(text=f"Your choice: {choice}")

    def play_round(self):
        """
        Play one round:
        - Randomly select computer's choice
        - Compare with the user's choice
        - Update and display results & scores
        """
        if not self.user_choice:
            messagebox.showwarning("No Choice", "Please choose rock, paper, or scissors before playing!")
            return

        # Computer randomly picks a move
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

        # Determine result
        result = self.determine_winner(self.user_choice, computer_choice)
        if result == "win":
            self.user_score += 1
            self.result_label.config(text="Result: You WIN! 🎉", fg="green")
        elif result == "lose":
            self.computer_score += 1
            self.result_label.config(text="Result: You LOSE! 😢", fg="red")
        else:
            self.result_label.config(text="Result: It's a TIE!", fg="blue")

        # Update score display
        self.score_label.config(text=self.get_score_text())

    @staticmethod
    def determine_winner(user, computer):
        """
        Game logic to determine winner based on the classic rules.
        Returns "win", "lose", or "tie".
        """
        user = user.lower()
        computer = computer.lower()
        if user == computer:
            return "tie"
        if ((user == "rock" and computer == "scissors") or
            (user == "scissors" and computer == "paper") or
            (user == "paper" and computer == "rock")):
            return "win"
        else:
            return "lose"

    def get_score_text(self):
        """
        Create a display string for current scores.
        """
        return f"Your Score: {self.user_score}   Computer Score: {self.computer_score}"

    def reset_scores(self):
        """
        Reset both scores and clear result display.
        """
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=self.get_score_text())
        self.result_label.config(text="Result: ")

# Run the game application!
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
