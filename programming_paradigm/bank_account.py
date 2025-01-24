class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes a BankAccount object with an optional initial balance (defaults to 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. New balance: {self.account_balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account if sufficient funds are available."""
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdrew {amount}. New balance: {self.account_balance}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be greater than 0.")
            return False

    def display_balance(self):
        """Displays the current account balance."""
            print(f"Current balance: {self.account_balance}")
