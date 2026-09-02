
#instence method
# class student:
#     def __init__(self,name):
#         self.name=name 
#     def show (self):
#         print(self.name)
# s=student("swathi")
# s.show()//self-->reference-->s here




#class method
# class demo:
#     @classmethod
#     def info(cls):
#         print("class method")
# demo.info()


#Sample Program – OOP in Action

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        print("Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.__balance)
        
account1 = BankAccount(1000)
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()