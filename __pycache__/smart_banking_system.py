from abc import ABC, abstractmethod


# 1. Customer Class
class Customer:
    bank_name = "XYZ Bank"

    def __init__(self, customer_name, account_number, balance, pin):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance
        self.__pin = pin

        print("Customer created successfully")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. Current Balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def check_balance(self):
        return self.balance

    # Getter & Setter for private variable
    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin

    # Magic Method
    def __str__(self):
        return f"Customer Name: {self.customer_name}, Balance: {self.balance}"

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        return self.balance + other.balance


# 2. Inheritance Example
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


# 3. Abstraction
class Loan(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


class HomeLoan(Loan):

    def calculate_interest(self):
        print("Home Loan Interest Calculated")


# 4. Duck Typing Example
class CreditCard:

    def pay(self):
        print("Payment via Credit Card")


class UPI:

    def pay(self):
        print("Payment via UPI")


def make_payment(payment_method):
    payment_method.pay()


# 5. Object Lifecycle
class Transaction:

    def __init__(self, txn_id):
        self.txn_id = txn_id
        print("Transaction Created")

    def __del__(self):
        print("Transaction Object Destroyed")


# 6. Class Method & Static Method
class BankUtility:

    interest_rate = 5

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @staticmethod
    def validate_ifsc(ifsc_code):
        return ifsc_code.startswith("ABC")