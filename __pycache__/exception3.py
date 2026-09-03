def divide (a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print("Error occurred inside divide()") 
        raise
    
try:
        result =  divide(10,0)
        print("result :", result)
        
except ZeroDivisionError:
        print("caller handled the error")