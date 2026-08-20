"""Number Guessing Game - Arch Technologies Month 2, Task 3."""

import random


MIN_NUMBER = 1
MAX_NUMBER = 100


def get_valid_guess() -> int:
    """Read and validate a guess from the player."""
    while True:
        user_input = input(f"Enter your guess ({MIN_NUMBER}-{MAX_NUMBER}): ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if MIN_NUMBER <= guess <= MAX_NUMBER:
            return guess

        print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")


def play_game() -> None:
    """Run one complete round of the number guessing game."""
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print("=" * 42)
    print("        NUMBER GUESSING GAME")
    print("=" * 42)
    print(f"I selected a number from {MIN_NUMBER} to {MAX_NUMBER}.")
    print("Try to guess it!\n")

    while True:
        guess = get_valid_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(f"\nCorrect! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s).")
            break


def main() -> None:
    """Let the player play repeatedly until they choose to stop."""
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if play_again != "y":
            print("Thanks for playing!")
            break

        print()


if __name__ == "__main__":
    main()
