# Python Development — Month 2, Task 4

## ATM Simulation

### Objective

The objective is to develop a command-line ATM simulation through Object-Oriented Programming. The application allows users to check their balance, deposit money, withdraw funds, and exit the system.

### Tools and technologies

- Python 3
- Visual Studio Code
- Command Prompt

### Implementation

The program contains an `ATM` class that encapsulates the account balance and implements balance inquiry, deposit, and withdrawal operations. The balance is stored as a private-style attribute named `_balance`. An `ATMController` class displays the menu, reads user input, validates amounts, and calls the appropriate `ATM` methods. The menu remains active through a loop until the user selects Exit.

Deposits are accepted only when the value is greater than zero. Withdrawals are rejected if the amount is invalid or exceeds the available balance. Exception handling prevents non-numeric amounts from crashing the application.

### Algorithm

1. Create an ATM account with an initial balance of Rs. 1,000.
2. Display the four-option ATM menu.
3. Read the user's selected option.
4. For balance inquiry, display the current balance.
5. For deposit, validate and add the entered amount.
6. For withdrawal, validate the amount and check available funds.
7. Display the updated balance after successful transactions.
8. Repeat the menu until the user chooses Exit.

### Testing performed

- Checked the initial balance.
- Deposited a valid positive amount.
- Rejected zero and negative deposits.
- Withdrew an amount within the available balance.
- Rejected a withdrawal greater than the balance.
- Tested non-numeric amounts.
- Tested an invalid menu option.
- Confirmed the Exit option ends the program.

### Result

The ATM Simulation was completed successfully. All required operations work correctly, the balance updates after valid transactions, and invalid transactions are handled safely.

### Screenshot checklist

Capture clear screenshots showing:

- Initial balance
- Successful deposit and updated balance
- Successful withdrawal and remaining balance
- Insufficient-balance message
- Exit message
