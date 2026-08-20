"""ATM Simulation - Arch Technologies Month 2, Task 4."""


class ATM:
    """Represent a simple ATM account and its banking operations."""

    def __init__(self, initial_balance: float = 1000.0) -> None:
        self._balance = initial_balance

    def check_balance(self) -> float:
        """Return the current account balance."""
        return self._balance

    def deposit(self, amount: float) -> bool:
        """Deposit a positive amount and report whether it succeeded."""
        if amount <= 0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount: float) -> tuple[bool, str]:
        """Withdraw money when the amount is valid and funds are available."""
        if amount <= 0:
            return False, "Amount must be greater than zero."

        if amount > self._balance:
            return False, "Insufficient balance."

        self._balance -= amount
        return True, "Withdrawal successful."


class ATMController:
    """Handle the menu and user interaction for an ATM object."""

    def __init__(self, atm: ATM) -> None:
        self.atm = atm

    @staticmethod
    def display_menu() -> None:
        print("\n" + "=" * 38)
        print("          ATM SIMULATION")
        print("=" * 38)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    @staticmethod
    def read_amount(prompt: str) -> float | None:
        """Read a numeric money amount or return None for invalid input."""
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return None

    def run(self) -> None:
        """Display the ATM menu until the user chooses to exit."""
        print("Welcome to the ATM!")

        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                print(f"Current balance: Rs. {self.atm.check_balance():,.2f}")

            elif choice == "2":
                amount = self.read_amount("Enter amount to deposit: Rs. ")
                if amount is None:
                    continue

                if self.atm.deposit(amount):
                    print(f"Deposit successful. New balance: Rs. {self.atm.check_balance():,.2f}")
                else:
                    print("Amount must be greater than zero.")

            elif choice == "3":
                amount = self.read_amount("Enter amount to withdraw: Rs. ")
                if amount is None:
                    continue

                success, message = self.atm.withdraw(amount)
                print(message)
                if success:
                    print(f"Remaining balance: Rs. {self.atm.check_balance():,.2f}")

            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid option. Please select a number from 1 to 4.")


def main() -> None:
    account = ATM(initial_balance=1000.0)
    controller = ATMController(account)
    controller.run()


if __name__ == "__main__":
    main()
