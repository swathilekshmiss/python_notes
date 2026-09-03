class InsufficientBalanceError(Exception):
    pass


class InvalidPINError(Exception):
    pass


class ATM:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.__pin = pin

    def validate_pin(self):
        try:
            entered_pin = int(input("Enter your PIN: "))

            if entered_pin != self.__pin:
                raise InvalidPINError("Incorrect PIN")

            print("PIN Verified Successfully")

        except ValueError:
            print("Please enter a valid numeric PIN")

        except InvalidPINError as error:
            print(error)

    def deposit(self):
        try:
            amount = int(input("Enter Deposit Amount: "))

            if amount <= 0:
                raise ValueError("Invalid Deposit Amount")

            self.balance += amount

        except ValueError as error:
            print("ValueError:", error)

        else:
            print("Deposit Successful")
            print("Current Balance:", self.balance)

    def withdraw(self):
        try:
            amount = int(input("Enter Withdrawal Amount: "))

            if amount <= 0:
                raise ValueError("Invalid Withdrawal Amount")

            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient Balance")

            self.balance -= amount

        except ValueError as error:
            print("ValueError:", error)

        except InsufficientBalanceError as error:
            print("InsufficientBalanceError:", error)

        else:
            print("Transaction Successful")
            print("Remaining Balance:", self.balance)

    def check_balance(self):
        try:
            print("Current Balance:", self.balance)

        except Exception as error:
            print("Unexpected Error:", error)

        else:
            print("Transaction Successful")


# Object Creation
customer = ATM(123456, 25000, 1234)


while True:
    print("\n------ ATM BANKING SYSTEM ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            customer.deposit()

        elif choice == 2:
            customer.withdraw()

        elif choice == 3:
            customer.check_balance()

        elif choice == 4:
            print("Thank You For Using ATM Banking System")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid numeric choice")

    finally:
        print("Session Processing...")

print("Session Closed Successfully")