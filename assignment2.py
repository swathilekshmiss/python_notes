#1  Check Even or Odd

# num=int(input("Enter a number :"))
# if num%2==0:
#        print("Number is Even")
# else:
#       print("Number is Odd")
      
#       output
#       Enter a number :8
# Number is Even

# Enter a number :9
# Number is Odd   


#2 Check Positive, Negative or Zero 

# num=int(input("enter a number :"))
# if num>0:
#     print("Number is Positive....")
# elif num<0:
#     print("Number is Negative....")
# else:
#     print("Number is Zero....") 
    
#     output
#     enter a number :10
# Number is Positive....

# enter a number :-7
# Number is Negative....

# enter a number :0
# Number is Zero....  

#3 Find the Largest of Two Numbers 

# num1=int(input("enter the first number : "))
# num2=int(input("enter the second number : "))
# if num1>num2:
#     print("num1 is larger")
# else:
#     print("num2 is larger")

# output
# enter the first number : 650
# enter the second number : 980
# num2 is larger 

#4  Find the Largest of Three Numbers

# num1=int(input("enter the first number : "))
# num2=int(input("enter the second number : "))
# num3=int(input("enter the third number : "))
# if num1>=num2 and num1>=num3:
#     print("num1 is larger")
# elif num2>=num3:
#     print("num2 is larger")
# else:
#         print("num3 is larger")
        
#         output
#   enter the first number : 100
# enter the second number : 150
# enter the third number : 200
# num3 is larger

#      enter the first number : 1000
# enter the second number : 850
# enter the third number : 150
# num1 is larger

#  enter the first number : 460
# enter the second number : 980
# enter the third number : 220
# num2 is larger


#5 Check Voting Eligibility

# age=int(input("enter your age : "))
# if age>=18:
#     print("you are eligible........")
# else:
#     print("you are  not eligible.....!!!!")
    
#     output
#     enter your age : 16
# you are  not eligible.....!!!!

# enter your age : 32
# you are eligible........

#6 Print Numbers from 1 to 10 

# for i in range(1,11):
#     print(i) 
    
#     output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10 


#7 Print Even Numbers from 1 to 20

# for i in range(2,21,2):
#     print(i)
# output
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

#8 Sum of First N Numbers

# num=int(input("enter the number : "))
# for i in range (n):
    
#9 Multiplication Table

# num=int(input("enter the number :" ))
# for i in range(1,11):
#     print(num, "x",i,"=",num*i )
    
    
# output
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

#10 Count from 1 to 10 Using While 

# i=1
# while i<=10:
#     print(i)
#     i=i+1
    
#     output
#     1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10  

#11 Reverse Counting

# i=10
# while i>=1:
#     print(i)
#     i=i-1

# output
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1  

#12 Sum Until User Enters 0

# result=0
# num=int (input("enter the number : "))
# while num !=0:
#     result=result+num
#     num = int(input("Enter the number: "))
# print(result)
  
  
# #   output
#   enter the number : 5
# Enter the number: 4
# Enter the number: 3
# Enter the number: 2
# Enter the number: 1
# Enter the number: 0
# 15  

#13 Skip Multiples of 3
# for i in range(1, 11):
#     if i % 3 == 0:
#         continue
#     print(i)
    
#     output
#     1
# 2
# 4
# 5
# 7
# 8
# 10

#14 Stop at Number 7

# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)
    
#     output
#     1
# 2
# 3
# 4
# 5
# 6  

#15 Print Only Odd Numbers

# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)
#         output
#         1
# 3
# 5
# 7
# 9 

#16 Find Factorial

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    

# num =int(input("enter a number :"))
# print("factorial of",num,"is",factorial(num))

# output
# enter a number :4
# factorial of 4 is 24  


#17 Count Digits

# num = int(input("Enter a number: "))

# count = 0

# while num > 0:
#     count = count + 1
#     num = num // 10

# print("Number of digits =", count)  

# output
# Enter a number: 3566
# Number of digits = 4  

#18 Reverse a Number

# num = int(input("Enter a number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reverse =", reverse)


# output
# Enter a number: 1234
# Reverse = 4321  

#20 Guess the Secret Number

# secret = 7

# guess = int(input("Enter your guess: "))

# while guess != secret:
#     print("Wrong! Try again.")
#     guess = int(input("Enter your guess: "))

# print("Correct! You guessed the secret number.")

# output
# Enter your guess: 5
# Wrong! Try again.
# Enter your guess: 3
# Wrong! Try again.
# Enter your guess: 7
# Correct! You guessed the secret number.