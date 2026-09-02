# def add(a,b):
# return (a + b)
# result=add(10,20)
# print(result)


# def add(a,b):
# print(a + b)
# result=add(10,20)
# print(result)   //ith correct IndentationError


# Function - A reusable block of code designed to perform a specific task

# Without function:
# print("Welcome")
# print("Welcome")
# print("Welcome")                   
# output
# Welcome
# Welcome
# Welcome    


#  With function:
# def welcome():
#     print("Welcome")
# welcome()
# welcome()
# welcome() 

# output
# Welcome
# Welcome
# Welcome      


# #  Function Definition
# def greet():
#     print("Hello")   


# print("A")
# def greet():
#     print("Hello")
# print("B")
# greet()
# output
# A
# B
# Hello   


# def add(a, b):
#     print(a + b)
# result = add(10, 20)
# print(result)
# output
# 30
# None   


# def add(a, b):
#     return a + b
# result = add(10, 20)
# Now: print(result)  
# output
# 30   


# def test():
#     print("A")
#     return
#     print("B")
# test()

# Output:A

# def stats(a, b):
#     return a + b, a * b
# s, p = stats(2, 4)
# print("Sum:", s)
# print("Product:", p)
# Output:
# Sum: 6
# Product: 8 


# Lambda Functions

# A lambda function is a small anonymous function created using the lambda keyword.
# # Normal Function
# def square(x):
#     return x * x
# Lambda
# pgm
# square = lambda x: x * x
# print(square(5)) 
# output:25  

# Multiple Arguments
# add = lambda a, b: a + b
# print(add(10, 20)) 
# output:30

# A. Positional Arguments - Values are matched according to their position.
# def greet(name, age):
#     print("Name:", name)
#     print("Age:", age)
# greet("Achu", 25)
# output
# Name: Achu
# Age: 25   

# B. Keyword Arguments
#// Pass arguments using parameter names.

# def greet(name, age):
#     print("Name:", name)
#     print("Age:", age)
# greet(age=25, name="Shivaay")

#// Here, order does not matter because the parameter names are specified.
# output
# Name: Shivaay
# Age: 25

#  C. Default Arguments
#// A parameter can have a default value.
# def greet(name="Guest"):
    # print("Hello", name)
# //Call with argument:
# greet("Rudra")     
# Output: Hello Rudra

# Call without argument:
# greet()        
# Output: Hello Guest




# Important Rule About Default Parameters.
# Valid:
# def student(name, age=18):
#     pass
# # Invalid:
# def student(name="Guest", age):
#     pass
# Generally, parameters without defaults must come before parameters with defaults.
# # Correct:
# def student(age, name="Guest"):
#     pass //its error yo after check




#multiple Arguments
# def total(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     return result

# print(total(10, 20))
# print(total(10, 20, 30))
# print(total(10, 20, 30, 40))

# output
# 30                      
# 60                    
# 100  //its tuple number 


# Multiple keyword arguments

# def student_info(**data):
#     for key, value in data.items():
#         print(key, ":", value)

# student_info(
#     name="Ravi",
#     age=18,
#     marks=85
# )
# output
# name : Ravi                
# age : 18                       
# marks : 85  //data dictionary form
# //*args → Many values (tuple)
# **kwargs → Many key=value pairs (dictionary)
