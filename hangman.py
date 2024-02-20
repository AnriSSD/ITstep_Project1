import random

# Constant for the maximum allowed errors
MAX_ERRORS = 7

# List of words for guessing
WORDS = [
    "python",
    "programming",
    "mentor",
    "hangman",
    "function",
    "student",
    "step",
    "hangman",
]


class Hangman:
    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess  # The word that needs to be guessed
        self.guessed_letters = set()  # The set of letters that have been guessed
        self.errors = 0  # Counter for the number of incorrect guesses

    # Method to display the current state of the guessed word
    def display_word(self):
        display = [
            letter if letter in self.guessed_letters else "_"
            for letter in self.word_to_guess
        ]
        return " ".join(display)

    # Method for a guess attempt
    def guess(self, letter):
        if letter in self.word_to_guess:
            self.guessed_letters.add(letter)
        else:
            self.errors += 1

    # Method to check if the player has won
    def is_won(self):
        return set(self.word_to_guess) <= self.guessed_letters

    # Method to check if the player has lost
    def is_lost(self):
        return self.errors >= MAX_ERRORS


# Function to run the game loop
def play_game():
    word_to_guess = random.choice(WORDS)
    game = Hangman(word_to_guess)

    print("Welcome to Hangman!")

    # The game loop continues until the player has won or lost
    while not game.is_won() and not game.is_lost():
        print("\nGuess the word: ", game.display_word())
        guess = input("Enter a letter or the whole word: ").lower()

        # Check for a valid single alphabet letter input
        if len(guess) == 1 and guess.isalpha():
            game.guess(guess)
        elif len(guess) == len(word_to_guess) and all(
            [letter.isalpha() for letter in guess]
        ):
            if guess == word_to_guess:
                game.guessed_letters = set(word_to_guess)
            else:
                game.errors += 1
        else:
            print("Please enter a single letter of the alphabet or the whole word.")

        print(f"Mistakes: {game.errors} out of {MAX_ERRORS}")

    # Check the outcome of the game
    if game.is_won():
        print(f"\nCongratulations! You have guessed the word: '{word_to_guess}'!")
    else:
        print(f"\nYou lost. The word was: '{word_to_guess}'.")


if __name__ == "__main__":
    play_game()
