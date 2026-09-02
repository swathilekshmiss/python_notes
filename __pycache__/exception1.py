# print("start")
# x=10/0
# print("end")///Traceback (most recent call last): 


try:
    a=10
    b=0
    if b==0:
        raise ZeroDivisionError("b cannot be zero")
    result = a / b
except ZeroDivisionError as e:
    print("cannot divide by zero!",e)
except Exception as e:
    print("unexpected error :",e)
else:
    print("result is :",result)
finally:
    print("cleanup completed")