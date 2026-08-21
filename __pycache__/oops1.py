# class student:
#     name="swathi"
# s.student()
# print(s.name)     


# class example:
#     __private = 3
# e = example()
# print(e.__private)//AttributeError: 'e




# class example:
#  __private = 3
# e = example()
# print(e._example__private)

#protected
# class account:
#     _balance = 1000
    
# class savingsaccount(account):
#     def show_balance(self):
#         print(self._balance)
# acc = savingsaccount()
# acc.show_balance()
# print(acc._balance)  



# single inheritend method  

# class animal:
#     def speak(self):
#         print("animal makes a sound")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# d=dog()
# d.speak()
# d.bark()  



# multilevel inheritance

# class animal:
#     def speak(self):
#         print("animal makes a sound")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# class puppy(dog):
#     def cry(self):
#         print("puppy cries")
# p=puppy()
# p.speak()
# p.bark()
# p.cry()



# hierarchial inherutance

# class animal:
#     def speak(self):
#         print("animal makes a sound")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
        
# class cat(animal):
#     def meow(self):
#         print("cat meow")             
# class puppy(dog):
#     def cry(self):
#         print("puppy cries")
# class kitten(cat):
#     def cryy(self):
#         print("kitten cries")
        
# p=puppy()
# p=kitten()
# p.speak()
# p.bark()
# p.meow()
# p.cry()
# p.cryy()  



# multiple inheritance 
# class father:
#     def driving(self):
#         print("father can drive")
        
# class mother:
#     def cooking(self):
#         print("mother can cook")
        
# class child(father,mother):
#     pass
# f=child()
# f.cooking()
# f.driving()

# //rule

# class father:
#     def driving(self):
#         print("father can drive")
        
# class mother:
#     def driving(self):
#         print("mother can cook")
        
# class child(father,mother):
#     pass
# f=child()
# f.driving()
# f.driving()

# MRO

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#         print("C")
# class D(B , C):
#     pass 
# d=D()
# d.show()  



# class animal:
#     def speak(self):
#         print("animal sound")
# class dog(animal):
#     def speak(self):
#         super().speak()
#         print("woof")
# d=dog()
# d.speak()

# QUESTION
# A bank wants to keep the customer's account balance protected.

# Create a class BankAccount with:

# account_holder as a public variable
# _balance as a protected variable
# __pin as a private variable

# Create an object and display the account holder and balance.

# # Task: Try accessing __pin directly. What happens?


# class BankAccount:
#     def __init__(self, account_holder, balance, pin):
#         self.account_holder = account_holder   # public
#         self._balance = balance                # protected
#         self.__pin = pin                       # private

#     def display(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: {self._balance}")


# # Create an object
# acc = BankAccount("Thara Krishna R", 50000, 1234)

# # Display account holder and balance
# acc.display()

# # Try accessing __pin directly
# # print(acc.__pin)   # AttributeError

# # Accessing private variable using name mangling
# print(acc._BankAccount__pin)


#  or

# class bankaccount:
#     accountholder="swathi"
#     _balance=1000
#     __pin=123
# d=bankaccount    
# print(d.accountholder)
# print(d._balance)
# print(d._bankaccount__pin)

# QUESTION
# A school has a general class Person.

# The Person class has:

# name
# age

# A Teacher is a type of Person.

# Create a Teacher class that inherits from Person and add:

# subject

# Create a teacher object and display all three details.








class Person:
    name = "MEENU"
    age = 25


class Teacher(Person):
    subject = "Python"


t = Teacher

print(t.name)
print(t.age)
print(t.subject)