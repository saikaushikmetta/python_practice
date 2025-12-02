# Mini Project – Guess the Number Game
# Concepts Used: while loop and user input.
# Sample Run:
# Guess a number between 1 and 10: 4
# Wrong guess! Try again.
# Guess again: 7
# Congratulations, Saumya! You guessed it right 🎉
import random
print("-----welcome to number guessing game-----")
user=int(input("enter number"))
secret_no=random.randint(1,10)
if user == secret_no:
    print("you won")
else:
    print("try again the number was:",secret_no)