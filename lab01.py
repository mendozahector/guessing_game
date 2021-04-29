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
    while True:
        difficulty = get_difficulty()
        guesses = start_game(difficulty)
        print_game_results(guesses)

        play_again = input("\nType any key to play again. Otherwise enter \"exit\" to quit game.\n"
            "> ")
        if play_again.lower() == "exit":
            break

# Game introduction
def welcome_message():
    print("This is the \"guess a number\" game.\n"
        "You try to guess a random number in the smallest number of attempts.\n")

# Prompt the user for how difficult the game will be. Ask for an integer
def get_difficulty():

    # Let's make sure we actually have an integer
    while True:
        try:
            integer = int(input("Pick a positive integer: "))
            if integer > 0:
                break
            else:
                print("Please pick a number greater than zero.")
        except ValueError:
            print("You have entered an invalid integer.")
    
    return integer

# Play the guessing game
def start_game(difficulty):

    # Generate a random number between 1 and the chosen value
    value_random = random.randint(1, difficulty)

    # Give the user instructions as to what he or she will be doing
    print(f"Guess a number between 1 and {difficulty}.")

    # Initialize the sentinal and the array of guesses
    guesses = []

    while True:
        # Prompt the user for a number
        try:
            guess = int(input("> "))

            # Store the number in an array so it can be displayed later
            guesses.append(guess)

            # Make a decision: was the guess too high, too low, or just right
            if guess == value_random:
                break
            elif guess > value_random:
                print("\tToo high!")
            elif guess < value_random:
                print("\tToo low!")

        # If input is valid we will display an error
        except ValueError:
            print("Please enter a valid number.")

    return guesses

# Give the user a report: How many guesses and what the guesses where
def print_game_results(guesses):
    num_guesses = len(guesses)

    if num_guesses == 1:
        print("Amazing! You guessed the number in one go!\n"
        "Your lucky number is:", guesses[0])
    else:
        print(f"You were able to find the number in {num_guesses} guesses\n"
        "The numbers you guessed were:", guesses)

if __name__ == "__main__":
    main()