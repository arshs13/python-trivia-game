"""
Hangman Game in Python
"""

# Importing necessary libraries
import random


def get_random_word(filename):
    """
    Function to read a list of words from a file and return a random word
    """
    with open(filename, "r") as file:
        words = file.readlines()
        return random.choice(words).strip()


def save_score(score, filename):
    """
    Function to save the score to a file
    """

    with open(filename, "a") as file:
        file.write(f"Score: {score}\n")


def hangman():
    """
    Main function to run the hangman game
    """
    # Initial setup
    word_to_guess = get_random_word("words.txt")  # Input from file
    guessed_letters = []  # List to keep track of guessed letters
    tries = 6  # Number of tries the user gets, can be changed as needed
    score = 0  # Initialize score

    print("Welcome to Hangman!")  # Output to display game start

    # Using a while loop for general iteration
    while tries > 0:
        # String to display the current state of guesses
        output = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                output += letter
            else:
                output += "_"

        # Check if the game is won
        if output == word_to_guess:
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            score += 10  # Increment score
            break

        print("Guess the word:", output)  # Output to display current guess status
        print(f"Tries left: {tries}")

        guess = input("Enter a letter: ")  # Taking input from the user

        # Analyze user's input
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print("Good guess!")
            score += 1  # Increment score for good guess
        else:
            guessed_letters.append(guess)
            print("Wrong guess!")
            tries -= 1  # Decrement tries if wrong guess

    if tries == 0:
        print(f"Game Over! The word was: {word_to_guess}")

    save_score(score, "scores.txt")  # Output to file


if __name__ == "__main__":
    hangman()  # Calling the main function to start the game
