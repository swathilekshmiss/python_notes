
# Question 1:Write a Python program to calculate the total bill.

# shirt=800
# shoes=1200
# total_bill=shirt+shoes
# print("Total Bill =",total_bill)
# output
# Total Bill = 2000


# Question:2
# A person has ₹10,000 in their bank account and withdraws ₹2,500. Find the remaining balance.

# current_balance =10000
# withdraw =2500
# remaining_balance =current_balance-withdraw
# print("Remaining Balance =",remaining_balance)
# output
# Remaining Balance = 7500  


# Question:3
# One movie ticket costs ₹250. A family buys 4 tickets. Calculate the total amount.  

# movie_ticket_cost =250
# buying_tickets =4
# total_amount = movie_ticket_cost * buying_tickets
# print("Total_Amount =",total_amount)
# output
# Total_Amount = 1000


# Question:4
# Four friends have a restaurant bill of ₹1,500. They want to divide it equally. How much should each person pay?

# restaurant_bill =1500
# total_person =4
# one_person_pay = restaurant_bill / total_person
# print("One_Person_Pay =",one_person_pay)
# output
# One_Person_Pay = 375.0


# Question:5
# A shop has 53 chocolates. Each box can hold 10 chocolates.
# Find:
# How many complete boxes can be filled?
# How many chocolates will be left? 

#chocolates =53
# box_holding =10
# complete_box = chocolates // box_holding
# remaining_chololates = chocolates % box_holding
# print("Complete Boxes =",complete_box)
# print(" Chocolates left =",remaining_chololates)

# output
# Complete Boxes = 5
#  Chocolates left = 3


# Question:6
# A movie is 145 minutes long. Find the number of complete hours and remaining minutes.

# movie_minutes =145
# hours = movie_minutes /60
# remaining_minutes = movie_minutes % 60
# print("complete hours =",hours)
# print("remaining minutes =",remaining_minutes)
# output
# complete hours = 2.4166666666666665
# remaining minutes = 25



# Question:7
# A teacher wants to check whether a student's roll number is even or odd.

# roll_number =int(input("enter  roll number :"))
# if roll_number % 2==0:
#     print("Even Number")
# else:
#     print("Odd Number")

# output
# enter  roll number :20
# Even Number

# enter  roll number :31
# Odd Number


# Question:8
# The side of a square is 5 metres. Calculate its area.
# Formula:
# Area = side² 

# one_side_square =5
# square_area = one_side_square ** 2
# print("Area of Square =",square_area)
# output
# Area of Square = 25


# Question:9
# A digital wallet has ₹500. The user adds ₹200. Update the balance.
# digital_wallet =500
# user_adds =200
# # balance =digital_wallet += user_adds // cannot used with another assignment.use it on the variable directly
# digital_wallet += user_adds
# print("Balance =",digital_wallet)

# output
# Balance = 700
 
 
# Question: 10
# A player starts with 100 points.
# Gains 50 points
# Loses 20 points
# Find the final score.

# start_points =100
# gain_points =50
# loss_points =20
# gain_points+=loss_points
# print("Total Points =",gain_points)
# start_points-= gain_points
# print("Final Score =",start_points)

# output
# Total Points = 70
# Final Score = 30 

# Question:11
# The passing mark is 40. A student scored 65. Check whether the student's mark is greater than or equal to the passing mark.

# passing_mark = 40
# student_score = 65
# student_score >= passing_mark
# print("The student has passed.")
# output
# The student has passed.



# Question:12
# A user enters a password. Check whether it matches the stored password.

# store_password ="swathi123"
# user_password =input("enter password :")
# if user_password == store_password:
#     print("Password correct.")
# else:
#     print("Password does not correct.")
    
#     output
#     enter password :swathi123
# Password correct.

# enter password :aswathi123
# Password does not correct.


# Question:13
# A shop wants to check whether the stock is not zero. 

# stock =50
# if stock !=0:
#     print("stock is available.")    
# output
# stock is available.



# Question:14
# A person can apply for a driving licence only if:
# Age is 18 or above AND
# They have passed the driving test

# age =18
# has_id =True
# if age >=18 and has_id:
#     print("apply for driving licence.")
# else:
#     print("Cannot apply for driving licence.")

# output
# apply for driving licence.


# age =15
# has_id =True
# if age >=18 and has_id:
#     print("apply for driving licence.")
# else:
#     print("Cannot apply for driving licence.")
# output
# Cannot apply for driving licence.


#question:15
#A day is considered a weekend if it is either Saturday OR Sunday.

# day="sunday"
# if day =="Saturday" or day=="sunday":
#    print("it is weekend")
   
#    output
#    it is weekend


#  Question:22
# list1 = [10, 20, 30]
# list2 = [10, 20, 30] 

# list1 = [10, 20, 30]
# list2 = [10, 20, 30]
# if list1==list2:
#     print("its equal......")
# output
# its equal......  


# Question:23
#     Same Object Reference
# cart1 = ["Laptop", "Mouse"]
# cart2 = cart1 

# cart1 = ["Laptop", "Mouse"]
# cart2 = cart1 
# print(cart1 is cart2)
# output
# True

# Question:18:
# A candidate is eligible for a job if:
# Age is at least 21
# Graduation is completed
# The candidate is not banned from applying
# age = 24  

# age=24
# graduation_completed=True
# banned=False 
# if age>=21 :
  