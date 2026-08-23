"""
Hangman
-------
A simple command-line Hangman game where the player guesses letters
to reveal a hidden fruit name before running out of attempts.
"""

import random

FRUIT_WORDS_EASY = ["Banana","Apple","Kiwi","Melon","Lemon","Mango","Grape"]
FRUIT_WORDS_MEDIUM = ["Orange","Avocado","Coconut","Apricot","Cherry","Papaya","Peach"]
FRUIT_WORDS_HARD = ["Quince","Fig","Kumquat","Persimmon","Pomegranate","Blackberry","Guava"]

ANIMAL_WORDS_EASY=["Cat","Lion","Rabbit","Tiger","Panda","Monkey","Dog"]
ANIMAL_WORDS_MEDIUM=["Dolphin","Giraffe","Elephant","Penguin","Cheetah","Kangaroo","Leopard"]
ANIMAL_WORDS_HARD=["Lynx","Jaguar","Chameleon","Platypus","Porcupine","Walrus","Hedgehog"]

COUNTRY_WORDS_EASY=["Canada","Japan","Italy","Brazil","Spain","France","China"]
COUNTRY_WORDS_MEDIUM=["Germany","Mexico","Vietnam","Portugal","Thailand","Egypt","Greece"]
COUNTRY_WORDS_HARD=["Kyrgyzstan","Luxembourg","Azerbaijan","Zimbabwe","Madagascar","Kazakhstan","Djibouti"]


MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """,
]

def choose_category() -> str:
    while True:
        print("\nCategories:\n1) Fruits\n2) Animals\n3) Countries")
        selected = input("Choose your category (1, 2, 3): ").strip()
        if selected == "1":
            return "fruits"
        elif selected == "2":
            return "animals"
        elif selected == "3":
            return "countries"
        else:
            print("Make a valid selection.")

def choose_difficulty() -> str:
    while True:
        print("\nDifficulty:\n1) Easy\n2) Medium\n3) Hard")
        selected = input("Choose your difficulty (1, 2, 3): ").strip()
        if selected == "1":
            return "easy"
        elif selected == "2":
            return "medium"
        elif selected == "3":
            return "hard"
        else:
            print("Make a valid selection.")

def choose_word(category: str, difficulty: str) -> str:
    if category == "fruits":
        if difficulty == "easy":
            return random.choice(FRUIT_WORDS_EASY)
        elif difficulty == "medium":
            return random.choice(FRUIT_WORDS_MEDIUM)
        else:
            return random.choice(FRUIT_WORDS_HARD)
    elif category == "animals":
        if difficulty == "easy":
            return random.choice(ANIMAL_WORDS_EASY)
        elif difficulty == "medium":
            return random.choice(ANIMAL_WORDS_MEDIUM)
        else:
            return random.choice(ANIMAL_WORDS_HARD)
    else:
        if difficulty == "easy":
            return random.choice(COUNTRY_WORDS_EASY)
        elif difficulty == "medium":
            return random.choice(COUNTRY_WORDS_MEDIUM)
        else:
            return random.choice(COUNTRY_WORDS_HARD)



    


def get_guess(letters_used: list[str]) -> str:
    """
    Prompt the player for a single, valid, not-yet-used letter.
    Keeps asking until the input is valid.
    """
    while True:
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        if guess in letters_used:
            print("You already tried that letter. Try a different one.")
            continue

        return guess


def update_puzzle(word: str, puzzle: str, guess: str) -> str:
    return "".join(
        letter if word[i].lower() == guess else puzzle[i]
        for i, letter in enumerate(word)
    )

def display_state(fail_count: int, puzzle: str, category: str, difficulty: str) -> None:
    """Print the current hangman drawing and the partially revealed word."""
    print(HANGMAN_STAGES[fail_count])
    print(f"Hint: [{category.capitalize()}] - [{difficulty.capitalize()}]")
    print(" ".join(list(puzzle)))


def play_round() -> None:
    
    print("Welcome to Hangman!")

    category = choose_category()
    difficulty = choose_difficulty()
    word = choose_word(category, difficulty)
    
    puzzle = "_" * len(word)
    letters_used: list[str] = []
    fail_count = 0


    while fail_count < MAX_ATTEMPTS:
        display_state(fail_count, puzzle, category, difficulty)
        guess = get_guess(letters_used)
        letters_used.append(guess)

        if guess in word.lower():
            puzzle = update_puzzle(word, puzzle, guess)
            if puzzle.lower() == word.lower():
                print(puzzle)
                print("Congratulations! You found the word.")
                return
        else:
            fail_count += 1

    display_state(fail_count, puzzle, category, difficulty)
    print("You lose!")
    print(f"The word was: {word}")


def main() -> None:
    play_round()

    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "y":
            print()
            play_round()
        elif again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please answer 'y' or 'n'.")


if __name__ == "__main__":
    main()
