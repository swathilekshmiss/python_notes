import sys

# Global balance
balance = 10000


# ---------------- CREATE ACCOUNT ----------------

def create_account(initial_amount):
    """Create a new account"""

    name = input("Enter your name: ")
    account_type = input("Enter account type: ")

    balance = initial_amount

    print("\nAccount Details")
    print("Name:", name)
    print("Account Type:", account_type)
    print("Balance:", balance)

    return balance


# ---------------- DEPOSIT ----------------

def deposit(balance, amount):
    """Deposit amount"""

    balance = balance + amount

    return balance


# ---------------- WITHDRAW ----------------

def withdraw(balance, amount):
    """Withdraw amount"""

    if amount <= balance:
        balance = balance - amount
        print("Amount Withdrawn Successfully")
    else:
        print("Insufficient Balance")

    return balance


# ---------------- CHECK BALANCE ----------------

def check_balance(balance):
    """Display current balance"""

    print("Current Balance:", balance)


# ---------------- PIN VERIFICATION ----------------

def pin_verification(attempt):
    """Recursive PIN verification"""

    print("PIN Verification Attempt:", attempt)

    # Base case
    if attempt == 3:
        print("Maximum Attempts Reached")
        return

    # Recursive case
    pin_verification(attempt + 1)


# ---------------- MAIN MENU ----------------

while True:

    print("\n------ ONLINE BANKING SYSTEM ------")

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---------------- CREATE ACCOUNT ----------------

    if choice == "1":

        initial_amount = float(
            input("Enter Initial Amount: ")
        )

        balance = create_account(initial_amount)


    # ---------------- DEPOSIT ----------------

    elif choice == "2":

        amount = float(
            input("Enter Deposit Amount: ")
        )

        balance = deposit(balance, amount)

        print("Amount Deposited Successfully")
        print("Updated Balance:", balance)

        # Lambda
        interest = lambda amount: amount * 0.05

        print("Interest Calculation using Lambda:")
        print(interest(balance))

        # filter()
        balances = [5000, 15000, 20000, 25000]

        high_balances = list(
            filter(
                lambda x: x > 10000,
                balances
            )
        )

        print("Accounts with Balance > 10000:")
        print(high_balances)

        # sorted()
        customer_names = [
            "Rahul",
            "Anu",
            "Sneha"
        ]

        sorted_names = sorted(customer_names)

        print("Sorted Customer Names:")
        print(sorted_names)

        # Recursion
        pin_verification(1)


    # ---------------- WITHDRAW ----------------

    elif choice == "3":

        amount = float(
            input("Enter Withdrawal Amount: ")
        )

        balance = withdraw(balance, amount)

        print("Updated Balance:", balance)


    # ---------------- CHECK BALANCE ----------------

    elif choice == "4":

        check_balance(balance)


    # ---------------- EXIT ----------------

    elif choice == "5":

        print("Thank you for using Online Banking System")
        break


    else:

        print("Invalid Choice")