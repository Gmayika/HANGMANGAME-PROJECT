import random

class Hangman:
    def __init__(self, word, category):
        self.word = word
        self.category = category
        self.remaining_attempts = 6
        self.guesses = set()

    def display_word(self):
        return ' '.join([letter if letter in self.guesses else '_' for letter in self.word])

    def make_guess(self, guess):
        self.guesses.add(guess)
        if guess not in self.word:
            self.remaining_attempts -= 1

    def is_game_over(self):
        return self.remaining_attempts <= 0 or '_' not in self.display_word()

    def display_hangman(self):
        hangman_art = [
            "-----\n|   |\n    |\n    |\n    |\n    |\n",
            "-----\n|   |\nO   |\n    |\n    |\n    |\n",
            "-----\n|   |\nO   |\n|   |\n    |\n    |\n",
            "-----\n|   |\nO   |\n/|  |\n    |\n    |\n",
            "-----\n|   |\nO   |\n/|\\ |\n    |\n    |\n",
            "-----\n|   |\nO   |\n/|\\ |\n/   |\n    |\n",
            "-----\n|   |\nO   |\n/|\\ |\n/ \\ |\n    |\n"
        ]

        stage = 6 - self.remaining_attempts
        print(hangman_art[stage])

class HangmanGame:
    def __init__(self):
        self.user_name = ""

    def get_user_name(self):
        self.user_name = input("Enter your name: ")
        print(f"Hello, {self.user_name}! Welcome to Hangman.")

    def play_hangman(self):
        self.get_user_name()

        while True:
            categories = ['animals', 'fruits', 'sports', 'colors', 'movies']
            selected_category = input("Choose a category (animals, fruits, sports, colors, movies): ").lower()

            while selected_category not in categories:
                print("Invalid category. Please choose from the provided list.")
                selected_category = input("Choose a category (animals, fruits, sports, colors, movies): ").lower()

            while True:
                word_to_guess, word_category = self.get_random_word(selected_category)

                hangman_game = Hangman(word_to_guess, word_category)

                while not hangman_game.is_game_over():
                    print("\n" * 100)  # Simulate clearing the console screen

                    print("\nCategory:", hangman_game.category)
                    print("Word:", hangman_game.display_word())
                    print("Attempts left:", hangman_game.remaining_attempts)

                    hangman_game.display_hangman()

                    guess = input("Enter a letter: ").lower()

                    if len(guess) == 1 and guess.isalpha():
                        hangman_game.make_guess(guess)
                    else:
                        print("Please enter a valid single letter.")

                if '_' not in hangman_game.display_word():
                    print("Correct! Well done.")
                else:
                    print("Sorry, you couldn't guess the word.")

                play_again = input("Do you want to play again in the same category? (yes/no): ").lower()
                if play_again != 'yes':
                    break

            change_category = input("Do you want to change the category and play again? (yes/no): ").lower()
            if change_category != 'yes':
                break

    def get_random_word(self, category):
        word_categories = {
            'animals': ['elephant', 'giraffe', 'tiger', 'monkey'],
            'fruits': ['apple', 'banana', 'orange', 'grape'],
            'sports': ['soccer', 'tennis', 'basketball', 'swimming'],
            'colors': ['red', 'blue', 'green', 'yellow'],
            'movies': ['avatar', 'inception', 'matrix', 'titanic']
        }

        if category not in word_categories:
            print("Invalid category. Using a random category.")
            category = random.choice(list(word_categories.keys()))

        return random.choice(word_categories[category]), category

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.play_hangman()
