# nums={1,2,2,3}
# print(nums)
# o/p 
# {1, 2, 3}

# nums=set([1,2,3,4])
# print(nums)
# print(type(nums)) 
# o/p 
# {1, 2, 3, 4}
# <class 'set'>


# empty={}
# print(type(empty))
# o/p 
# <class 'dict'> //wrong method to  create empty set
# correct way to create empty set
# empty=set()
# print(type(empty))  //<class 'set'> 

# nums={10,20,30}
# print(nums[0]) //TypeError:
#  acces set
# nums={10,20,30}
# for item in nums:
#     print(item)
#     o/p 
#     10
# 20
# 30 

# add element
# nums={1,2}
# nums.add(3)
# print(nums)
# o/p 
# {1, 2, 3} 

# existing element
# nums={1,2}
# nums.add(2)
# print(nums) //{1, 2} 

# update set 
# nums={1,2}
# nums.update([3,4,5])
# print(nums)
# // {1, 2, 3, 4, 5} 

# nums={1,2}
# nums.update({3,4,5})
# print(nums)
# // {1, 2, 3, 4, 5} 

# remove element 
# nums={1,2,3}
# nums.remove(2)
# print(nums)
# // {1,3} 

# nums={1,2,3}
# nums.remove(4)
# print(nums)
# //KeyError: 4 

# discard 
# nums={1,2,3}
# nums.discard(2)
# print(nums)
# // {1,3} 

# pop()
# nums={1,2,3}
# x = nums.pop()
# print(x) 
# // 1 expect 2 or 3  

# clear() 
# nums={1,2,3,4,5}
# nums.clear()
# print(nums)  //set() 

# union 
# a={1,2,3}
# b={3,4,5}
# print(a|b) //{1, 2, 3, 4, 5} 

# intersection
# a={1,2,3}
# b={3,4,5}
# print(a&b)//{3}

# difference
# a={1,2,3}
# b={3,4,5}
# print(a-b) //{1,2} 


# symmetric difference 
# a={1,2,3}
# b={3,4,5}
# print(a^b) //{1, 2, 4, 5} 

# membership testing 
# nums={1,2,3}
# print(2 in nums) // true
# print(4 in nums) // False 



# iterating over sets
# nums={1,2,3} 
# for item in nums:
#     print(item)
#     //1
# 2
# 3  



# frozenset-immutable set 
# nums=frozenset([1,2,3])
# nums.add(4)
# nums.remove(2)
# // AttributeError


# dictionary 

# student={
    
#     "name": "Alice",
#     "age": 30,
#     "course": "python"
# }

# print(student)

# o/p 
# {'name': 'Alice', 'age': 30, 'course': 'python'} 


# can values repeat? 
# data = {
#     "A":100,
#     "B":100
# }
# print(data) //{'A': 100, 'B': 100}

# can keys repeat?
# student = {
#     "name": "rahul",
#     "name":"achu"
# }
# print(student) //{'name': 'achu'}  

# person dict(
#     "name"="ammukutti",
#     "city"="kohinoor",
#     age=20
# )
# print(person)  

# student ={
#     "name":"rahul",
#     "age":20
# }
# print(student["name"])//rahul
# print(student["city"])//key KeyError 

# student ={
#     "name":"rahul",
#     "age":20
# }
# student.get ("name") 

# update values
# student ={
#     "name":"rahul",
#     "age":20
# }
# student["age"] = 21
# print(student["age"])//21

# student ={
#     "name":"rahul",
#     "age":20
# }
# student["age"] = 21
# student.update({"city":"chennai","grade":"A"})
# print(student)
# // {'name': 'rahul', 'age': 21, 'city': 'chennai', 'grade': 'A'}


# remove-pop()

# student ={
#     "name":"rahul",
#     "age":20
# }
# x =student.pop("age")
# print(x)//20  


# student ={
#     "name":"rahul",
#     "age":20
# }
# del student["age"]
# print(student) //{'name': 'rahul'}  

# Iterating
# student ={
#     "name":"rahul",
#     "age":20
# }
# for key in student:
#     print(key) //name
# age  

# student ={
#     "name":"rahul",
#     "age":20
# }
# for value in student.values():
#     print(value)
# // rahul
# 20


# student ={
#     "name":"rahul",
#     "age":20
# }
# for key,value in student.items():
#     print(key,value)  //
    
#     name rahul
# age 20  




# membership 
# student ={
#     "name":"rahul",
#     "age":20
# }
# print("rahul" in student.values())  //True 


# mixed data types 
# data = {
#     1:"one",
#     "two":2,
#     (3,4):"tuple"
# }
# print(data) //{1: 'one', 'two': 2, (3, 4): 'tuple'}


# data = {
#     1:"one",
#     "two":2,
#     [3,4]:"tuple"
# }
# print(data)//TypeError  


# nested dictionary 
# student ={
#     "name":"rahul",
#     "marks":{
#         "math":90,
#         "science":85
#     }
# }
# print(student["marks"]["math"])
# // 90