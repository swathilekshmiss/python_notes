# //local variable
# def show():
#     x = 10
#     print(x)

# show()

# output==10



# //Global variable
# x =10
# def show():
#     x = 20
# print(x)
# show()
# print(x)

# output==10
# 10

# //The nonlocal keyword is used inside a nested function to modify a variable that belongs to the outer (enclosing) function, not the global scope.

# def outer():
#     x = "outer"

#     def inner():
#         nonlocal x
#         x = "inner"

#     inner()
#     print("x after inner():", x)

# outer()


# output== x after inner(): inner 


# //The LEGB Rule tells Python where to look for a variable when it sees a variable name.

# LEGB stands for:

# L → Local
# E → Enclosing
# G → Global
# B → Built-in



# x = "global"

# def outer():
#     x = "enclosing"

#     def inner():
#         x = "local"
#         print("Inner x:", x)

#     inner()
#     print("Outer x:", x)

# outer()
# print("Global x:", x)


# output
# Inner x: local
# Outer x: enclosing
# Global x: global  




# Recursion
# Recursion means a function calls itself.
# def coutdown(n):
#     print(n)
#     if n > 1:
#         coutdown(n-1)
# coutdown(5)

# output:
# 5
# 4
# 3
# 2
# 1





# task : factorial of  a number using recursion
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# num1 = int(input("Enter the number: "))
# result = factorial(num1)
# print("The factorial is:", result)   


# output
# Enter the number: 2
# The factorial is: 2

# Enter the number: 10
# The factorial is: 3628800  

# Enter the number: 15
# The factorial is: 1307674368000

# Enter the number: 0
# The factorial is: 1

# Enter the number: 1
# The factorial is: 1








