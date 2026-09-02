# //sorted
# nums=[3,2,1]
# new_list = sorted(nums)
# print(nums)
# print(new_list)
# o/p
# [3, 2, 1]
# [1, 2, 3]

# nums =[10,20,30,40]
# reverse=nums[::-1]
# print(nums)
# print(reverse)  

# o/p 
# [10, 20, 30, 40]
# [40, 30, 20, 10]  


# //list itrerate
# fruits=["apple","banana","mango"]
# for fruit in fruits:
#     print(fruit)
    
#     o/p 
#     apple
# banana
# mango  

# another way 
# fruits=["apple","banana","mango"]
# for i in range(len(fruits)):
#     print(fruits[i])
#     o/p 
#     apple
# banana
# mango  

# membership operators
# nums=[1,2,3]
# print(2 in nums)
# o/p 
# True


# nums=[1,2,3]
# print(5 not in nums)
# o/p 
# True  

# concatenation  
# a=[1,2]
# b=[3,4]
# print(a+b)
# o/p 
# [1, 2, 3, 4] 

# repetition 
# a=[1,2]
# print(a*2)
# o/p 
# [1, 2, 1, 2] 

# nested list 
# matrix=[[1,2],[3,4]]
# print(matrix[0])
# print(matrix[1])

# o/p 
# [1, 2]
# [3, 4]  

# matrix=[[1,2],[3,4]]
# print(matrix[0])
# print(matrix[1])
# print(matrix[0][1])
# print(matrix[1][0])
 
#  o/p 
#  [1, 2]
# [3, 4]
# 2
# 3  

# //tuple 
# numbers=(1,2,3,4)
# print(type(numbers)) 
# o/p 
# <class 'tuple'>  

# empty=()
# print(type(empty))

# o/p 
# <class 'tuple'> 

# t1=(5)
# print(type(t1))
# o/p 
# <class 'int'> 

# t1=(5 ,)
# print(type(t1))

# o/p 
# <class 'tuple'> 
# a = 10,20
# print(type(a))
# o/p 
# <class 'tuple'>  


# //unpacking 
# point = (10,20)
# x,y =point
# print(x)
# print(y)  
# o/p 
# 10
# 20

# point = (10,20)
# x,y,z =point
# print(x)
# print(y)  
# //ValueError: 
# tuple slicing
# num=(10,20,30,40,50)
# print(num[1:4])
# o/p 
# (20, 30, 40)

# 

# nums=(1,2,2,3)
# print(nums.count(2))
# o/p 
# 2
# nums=(10,20,30)
# print(nums.index(20))
# o/p 
# 1 

# color=("red","green","blue")
# for clr in colors:
#     print(color)  
# without tuple unpacking



# with tuple unpacking

#extended unpacking
# nums=(1,2,3,4,5)
# a,b,*c=nums
# print("a=",a)
# print("b=",b)
# print("c=",c)
# o/p 
# a= 1
# b= 2
# c= [3, 4, 5] 

# Converting Between List and Tuple

nums_list=[1,2,3]

nums_tuple=tuple(nums_list)

nums_list=list(nums_tuple)