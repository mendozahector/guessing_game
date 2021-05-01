# 1. Name:
#    Hector Mendoza
# 2. Assignment Name:
#    Lab 01: Python Review
# 3. Assignment Description:
#    User is asked to enter a number. Then the program computes
#    a random number between 1 and the specified number.
#    The user is then asked to guess this random number,
#    with hints if the input number is "too high" or "too low".
#    Finally, after correcting guessing the number, the user
#    is congratulated followed by a display of all of the guesses.
# 4. What was the hardest part? Be as specific as possible.
#    This was a basic assignment to practice Python, and I had no major
#    difficulties.
#    What did take sometime was playing around with the while loops, and
#    also digging a little bit into the Try Except, in order to correctly
#    handle invalid inputs entered by the user. Hope I implemented them
#    correctly.
# 5. How long did it take for you to complete the assignment?
#    2 hours.

import random

def main():
    welcome_message()

    # We keep playing until the user exits the game
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

    # We make sure the user enters a valid input
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

    # We display the correct message, according to the number of guesses
    if num_guesses == 1:
        print("Amazing! You guessed the number in one go!\n"
        "Your lucky number is:", guesses[0])
    else:
        print(f"You were able to find the number in {num_guesses} guesses\n"
        "The numbers you guessed were:", guesses)

if __name__ == "__main__":
    main()