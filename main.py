import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Choices
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

# ASCII Art for a fun UI
def display_banner():
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + " 🎮 WELCOME TO ROCK-PAPER-SCISSORS! 🎮 ")
    print(Fore.CYAN + "=" * 40)

def get_winner(user, computer):
    global user_score, computer_score

    if user == computer:
        return "🤝 It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        user_score += 1
        return Fore.GREEN + "🎉 You win!"
    else:
        computer_score += 1
        return Fore.RED + "💀 You lose!"

def play_game():
    global user_score, computer_score

    while True:
        display_banner()

        # Get user input
        user_choice = input(Fore.CYAN + "Enter Rock, Paper, or Scissors: ").lower()
        
        if user_choice not in choices:
            print(Fore.RED + "⚠️ Invalid choice. Please try again.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(choices)
        
        # Show choices
        print(Fore.YELLOW + "\n🧑 You chose:", Fore.BLUE + user_choice.capitalize())
        time.sleep(1)
        print(Fore.MAGENTA + "🤖 Computer chose:", Fore.BLUE + computer_choice.capitalize())
        time.sleep(1)

        # Determine the winner
        result = get_winner(user_choice, computer_choice)
        print(Fore.CYAN + "\n" + result)

        # Show scores
        print(Fore.GREEN + f"\n📊 Score: You {user_score} - {computer_score} Computer\n")

        # Ask to play again
        again = input(Fore.BLUE + "Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print(Fore.YELLOW + "\n👋 Thanks for playing! Final Score:")
            print(Fore.GREEN + f"📊 You {user_score} - {computer_score} Computer")
            break

# Run the game
play_game()
