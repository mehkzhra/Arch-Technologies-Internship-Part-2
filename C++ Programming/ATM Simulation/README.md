# ATM Simulation in C++

Arch Technologies Internship — C++ Programming, Month 2, Task 4.

## Project overview

This project is a command-line ATM Simulation developed in C++ using Object-Oriented Programming. It allows users to check their account balance, deposit money, withdraw available funds, and exit safely.

The project is compiled and executed in Google Colab, so no local C++ compiler is required.

## Features

- Balance inquiry
- Deposit operation with amount validation
- Withdrawal operation with insufficient-balance protection
- Invalid menu and non-numeric input handling
- Initial account balance of Rs. 1,000
- Currency values displayed with two decimal places
- Object-Oriented Programming using `ATM` and `ATMController` classes
- Encapsulation of the account balance

## Technologies used

- C++17
- Google Colab
- GNU g++ compiler available in Colab

## Run the project in Google Colab

### Step 1: Create a notebook

Open [Google Colab](https://colab.research.google.com/) and select **File → New notebook**.

Rename the notebook:

```text
C++_Month2_Task4_ATM_Simulation.ipynb
```

### Step 2: Create the C++ source file

Add a code cell. Type the following line first and paste the complete contents of `atm_simulation.cpp` underneath it:

```cpp
%%writefile atm_simulation.cpp

// Paste the complete C++ ATM Simulation code here.
```

Run the cell. Colab should display:

```text
Writing atm_simulation.cpp
```

### Step 3: Compile the program

Add and run a second code cell:

```python
!g++ -std=c++17 atm_simulation.cpp -o atm_simulation
```

If the cell finishes without an error, compilation was successful.

### Step 4: Run the program

Add and run a third code cell:

```python
!./atm_simulation
```

## Recommended test sequence

Use the following menu options and amounts:

```text
1
2
500
3
300
3
5000
4
```

This sequence demonstrates:

1. Initial balance of Rs. 1,000
2. Successful Rs. 500 deposit
3. Successful Rs. 300 withdrawal
4. Insufficient balance for a Rs. 5,000 withdrawal
5. Safe program exit

## Expected output

```text
Welcome to the ATM!

======================================
          ATM SIMULATION
======================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 1
Current balance: Rs. 1000.00

Choose an option (1-4): 2
Enter amount to deposit: Rs. 500
Deposit successful.
New balance: Rs. 1500.00

Choose an option (1-4): 3
Enter amount to withdraw: Rs. 300
Withdrawal successful.
Remaining balance: Rs. 1200.00

Choose an option (1-4): 3
Enter amount to withdraw: Rs. 5000
Insufficient balance.

Choose an option (1-4): 4
Thank you for using the ATM. Goodbye!
```

## Save the notebook

After successfully running the project, download the notebook:

```text
File → Download → Download .ipynb
```

Place the notebook inside the ATM Simulation project folder.

## Screenshot requirements

Capture clear screenshots showing:

- Google Colab notebook title
- Successful compilation cell
- Initial account balance
- Successful deposit and updated balance
- Successful withdrawal and remaining balance
- `Insufficient balance` message
- Exit message

Save the screenshot as:

```text
atm_simulation_output.png

```

## Concepts demonstrated

- Classes and objects
- Constructors
- Encapsulation
- Methods and references
- Loops and conditional statements
- Input validation
- Formatted output
- Basic banking transaction logic
