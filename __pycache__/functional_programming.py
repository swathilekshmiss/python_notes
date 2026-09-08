# def greet():
#     print("hello")
# # x=greet
# # x() // store the function in a variable 
# x = greet()//returen the result to store

def squre(x):
    return x*x
def calculate(func,value):
    return func(value)
result = calculate (squre ,5)
print(result)