# Python Development — Month 2, Task 3

## Number Guessing Game

### Objective

The objective of this project is to create an interactive Python game in which the computer randomly chooses a number between 1 and 100. The player repeatedly guesses the number and receives a hint indicating whether the guess is too high or too low.

### Tools and technologies

- Python 3
- Visual Studio Code
- Built-in Python `random` module

### Implementation

The program uses `random.randint(1, 100)` to generate the secret number. A `while` loop continues accepting guesses until the player enters the correct value. Conditional statements compare each guess with the secret number and display an appropriate hint. A separate validation function handles non-numeric values and numbers outside the permitted range. The program also records the total number of valid attempts and allows the player to start another round.

### Algorithm

1. Generate a random integer between 1 and 100.
2. Set the attempt counter to zero.
3. Ask the player to enter a guess.
4. Validate that the input is a whole number from 1 to 100.
5. Increase the attempt counter.
6. Display “Too low” when the guess is smaller than the secret number.
7. Display “Too high” when the guess is greater than the secret number.
8. When both numbers match, display the result and number of attempts.
9. Ask whether the player wants to play again.

### Testing performed

- Entered a number lower than the secret number.
- Entered a number higher than the secret number.
- Entered the correct number.
- Entered text instead of a number.
- Entered numbers below 1 and above 100.
- Tested both replay and exit choices.

### Result

The Number Guessing Game was completed successfully. It generates a random number, validates player input, provides accurate hints, counts attempts, and supports multiple game rounds.

### Screenshot checklist

Capture one clear terminal screenshot showing:

- The game title
- At least one “Too high” response
- At least one “Too low” response
- The final correct answer and attempt count
- The exit message
