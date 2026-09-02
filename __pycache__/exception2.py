def age_checker(age):
    if age < 0:
     raise ValueError("age cannot be negative")
    return age
try:
    print("age is ", age_checker(-5))   
except ValueError as e:
    print("Error:", e)