import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount object with an optional initial balance.
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        print("Operations: deposit, withdraw, balance")
        return

    operation = sys.argv[1].lower()

    if operation == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            return
        try:
            amount = float(sys.argv[2])
            account.deposit(amount)
        except ValueError:
            print("Please provide a valid amount for deposit.")
    
    elif operation == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            return
        try:
            amount = float(sys.argv[2])
            account.withdraw(amount)
        except ValueError:
            print("Please provide a valid amount for withdrawal.")

    elif operation == "balance":
        account.display_balance()

    else:
        print("Invalid operation. Valid operations: deposit, withdraw, balance.")

if __name__ == "__main__":
    main()
