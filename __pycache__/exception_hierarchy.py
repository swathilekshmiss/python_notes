# try:
#     x = 10 / 0
    
# except ZeroDivisionError:
#     print("cannot divide by zero")
    
# except Exception:
#     print("General error")





# try:
#     val = int ("swathi")
# except (ValueError, TypeError) as e:
#     print("Invalid input:", e)  



# try:
#     val = None ("swathi")
# except (ValueError, TypeError) as e:
#     print("Invalid input:", e)  



# try:
#     f = open("data.txt", "r")
#     try:
#         data = f.read()
#         number = int (data)
#     except ValueError:
#         print("file does not contain a valid integer")
#     finally:
#         f.close()
# except FileNotFoundError:
#     print("file not found")



class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self,balance =0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"attempted to withdraw {amount},but only {self.balance} available")
        
        self.balance -= amount
        
b=BankAccount(10000)
b.withdraw(5000)
print("withdraw successful, remaining balance :",b.balance)