# Number Guessing Game in C++

Arch Technologies Internship â€” C++ Programming, Month 2, Task 3.

## Project overview

This project is an interactive C++ Number Guessing Game. The computer randomly selects a number between 1 and 100. The player repeatedly enters guesses, and the program reports whether each guess is too high or too low until the correct number is found.

The project is compiled and executed in Google Colab, so a local C++ compiler is not required.

## Features

- Random number generation from 1 to 100
- Too-high and too-low hints
- Input validation for text and out-of-range values
- Attempt counter
- Option to play another round
- Beginner-friendly C++ implementation

## Technologies used

- C++17
- Google Colab
- GNU g++ compiler available in Colab

## Run the project in Google Colab

### Step 1: Create a notebook

Open [Google Colab](https://colab.research.google.com/) and select **File â†’ New notebook**.

Rename the notebook:

```text
C++_Month2_Task3_Number_Guessing_Game.ipynb
```

### Step 2: Create the C++ source file

Add a code cell, type `%%writefile number_guessing_game.cpp` on its first line, and paste the complete contents of `number_guessing_game.cpp` below it:

```cpp
%%writefile number_guessing_game.cpp

// Paste the complete C++ source code here.
```

Run the cell. Colab should display:

```text
Writing number_guessing_game.cpp
```

### Step 3: Compile the program

Add and run another code cell:

```python
!g++ -std=c++17 number_guessing_game.cpp -o number_guessing_game
```

If the cell finishes without an error, compilation was successful.

### Step 4: Run the game

Add and run the following cell:

```python
!./number_guessing_game
```

Enter guesses in the input box until the correct number is found. Type `n` when the program asks whether you want to play again.

## Expected behavior

```text
==========================================
        NUMBER GUESSING GAME
==========================================
I selected a number from 1 to 100.
Try to guess it!

Enter your guess (1-100): 50
Too high! Try a lower number.

Enter your guess (1-100): 25
Too low! Try a higher number.

Enter your guess (1-100): 37
Correct! The number was 37.
You guessed it in 3 attempt(s).

Would you like to play again? (y/n): n
Thanks for playing!
```

The secret number and number of attempts will differ because the number is generated randomly.

## Save the work

Download the completed notebook using:

```text
File â†’ Download â†’ Download .ipynb
```

Place the downloaded notebook in the project folder.

## Screenshot requirements

Capture clear screenshots showing:

- Google Colab notebook title
- Successful compilation cell
- Game heading
- At least one `Too high` response
- At least one `Too low` response
- Correct number and attempt count
- `Thanks for playing!` message

Save the screenshot as:

sample_output.png

```
## Concepts demonstrated

- Variables and constants
- Functions
- `while` and `do-while` loops
- Conditional statements
- Random number generation
- Standard input and output
- Input validation