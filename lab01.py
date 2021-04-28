# 1. Name:
#    Hector Mendoza
# 2. Assignment Name:
#    Lab 01: Python Review
# 3. Assignment Description:
#    -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#    -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  

import random

def main():
    welcome_message()
    difficulty = get_difficulty()

    print(f"Guess a number between 1 and {difficulty}")

# Game introduction
def welcome_message():
    print("This is the \"guess a number\" game.\n"
        "You try to guess a random number in the smallest number of attempts.\n")

# Prompt the user for how difficult the game will be. Ask for an integer
def get_difficulty():
    # Let's make sure we actually have an integer
    while True:
        try:
            integer = int(input("Pick a positive integer (greater than 1): "))
            if integer > 1:
                break
            else:
                print("Please pick a number greater than 1.")
        except ValueError:
            print("You have entered an invalid integer.")
    
    return integer

# Generate a random number between 1 and the chosen value
#value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing

# Initialize the sentinal and the array of guesses

# Play the guessing game

    # Prompt the user for a number

    # Store the number in an array so it can be displayed later

    # Make a decision: was the guess too high, too low, or just right

# Give the user a report: How many guesses and what the guesses where

if __name__ == "__main__":
    main()