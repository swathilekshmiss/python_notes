# word = "malayalam"
# count = {}


# for ch in word:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1


# highest = 0
# second = 0
# most_char = ""
# second_char = ""


# for ch in count:
#     if count[ch] > highest:
#         second = highest
#         second_char = most_char


#         highest = count[ch]
#         most_char = ch
#     elif count[ch] > second:
#         second = count[ch]
#         second_char = ch


# print("Second most frequent character:", second_char)  


# for i in range(5):
#     print("*",end="")//horizondal print 

# for i in range(5):
#     print("*")//vertical print 


# for i in range(1,10):
#     for j in range(i):
#         print("*",end="")
#     print() // piramid 

# or 

# for i in range(1,10,1):
#     print(i*"*")  




# n=10
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
    
    
    
# for i in range(1,7):
#         print()
#         for j in range(1,i+1):
#             print(j,end="")


    
# for i in range(a,k):
#         print()
#         for j in range(a,i):
#             print(j,end="")





n=4
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end="")
        num+=1
    print()