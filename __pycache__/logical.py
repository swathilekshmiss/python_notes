# 1. Count Frequency of Each Character

# text="banana"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# highest=0
# frequent=""
# for ch in count:
#     if count[ch]>highest:
#         highest=count[ch]
#         frequent=ch
# print("most frequent character :", frequent)  

# //output--->   {'b': 1, 'a': 3, 'n': 2}
# most frequent character : a



# 2. Find the Least Frequent Character

# text = "malayalam"
# count = {}

# for ch in text:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1

# print(count)

# least = 10
# frequent = ""

# for ch in count:
#     if count[ch] < least:
#         least = count[ch]
#         frequent = ch

# print("least frequent character :", frequent)

# //output--->  {'m': 2, 'a': 4, 'l': 2, 'y': 1}
# least frequent character : y



# 3. Find Characters Appearing More Than Once

# word = "malayalam"
# count = {}

# for ch in word:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1

# print(count)

# for ch in count:
#     if count[ch] > 1:
#         print("character:", ch) 
        
#   //output---->      {'m': 2, 'a': 4, 'l': 2, 'y': 1}
# character: m
# character: a
# character: l  



#4. Find Characters Appearing Exactly Once
# word = "malayalam"
# count = {}


# for ch in word:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1


# for ch in count:
#     if count[ch] == 1:
#         print("Character:", ch)
#         //output--->Character: y
        
        
        #5. Find the First Repeated Character
# word = "malayalam"
# seen = set()


# for ch in word:
#     if ch in seen:
#         print("First repeated character:", ch)
#         break
#     else:
#         seen.add(ch)
        
#         output---> First repeated character: a 



#6. Find the First Non-Repeated Character
# word = "malayalam"
# count = {}


# for ch in word:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1


# for ch in word:
#     if count[ch] == 1:
#         print("First non-repeated character:", ch)
#         break 
    
    # output--->  First non-repeated character: y  
    
    
    
    #7. Find the Second Most Frequent Character
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


# output--->  Second most frequent character: m  



#8. Find the Number of Unique Characters
# word = "malayalam"
# count = {}


# for ch in word:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1


# print("Number of unique characters:", len(count))  

# output--->  Number of unique characters: 4  



#9. Find the Most Frequent Number


# numbers = [2, 3, 2, 5, 3, 2, 4, 3]
# count = {}


# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1


# highest = 0
# frequent = ""


# for num in count:
#     if count[num] > highest:
#         highest = count[num]
#         frequent = num


# print("Most frequent number:", frequent)

# output--->  Most frequent number: 2  



#10. Find the Least Frequent Number
# numbers = [2, 3, 2, 5, 3, 2, 4, 3]
# count = {}


# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1


# least = 10
# frequent = ""


# for num in count:
#     if count[num] < least:
#         least = count[num]
#         frequent = num


# print("Least frequent number:", frequent) 

# output--->Least frequent number: 5  



#11. Most Purchased Product

# orders = ["Laptop", "Mouse", "Laptop", "Keyboard",
#           "Mouse", "Laptop"]


# count = {}

# for product in orders:
#     if product in count:
#         count[product] += 1
#     else:
#         count[product] = 1


# highest = 0
# most_purchased = ""


# for product in count:
#     if count[product] > highest:
#         highest = count[product]
#         most_purchased = product


# print("Most purchased product:", most_purchased) 

# output---> Most purchased product: Laptop 



#12. Most Common Vote

# votes = ["A", "B", "A", "C", "B", "A", "B"]

# count = {}

# for vote in votes:
#     if vote in count:
#         count[vote] += 1
#     else:
#         count[vote] = 1

# highest = 0
# most_common = ""

# for vote in count:
#     if count[vote] > highest:
#         highest = count[vote]
#         most_common = vote

# print("Most common vote:", most_common)

# output--->  Most common vote: A  



#13. Most Common Word

# text = "apple mango apple orange mango apple"

# words = text.split()

# count = {}

# for word in words:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1

# highest = 0
# most_common = ""

# for word in count:
#     if count[word] > highest:
#         highest = count[word]
#         most_common = word

# print("Most common word:", most_common)

# output--->  Most common word: apple  



#14. Most Common Student Name

# names = ["Anu", "Rahul", "Anu", "Meera", "Rahul", "Anu"]

# count = {}

# for name in names:
#     if name in count:
#         count[name] += 1
#     else:
#         count[name] = 1

# highest = 0
# most_common = ""

# for name in count:
#     if count[name] > highest:
#         highest = count[name]
#         most_common = name


# print("Most common student name:", most_common)


# output--->  Most common student name: Anu 


#15. Most Common Error Code

# errors = [404, 500, 404, 403, 404, 500]

# count = {}

# for error in errors:
#     if error in count:
#         count[error] += 1
#     else:
#         count[error] = 1

# highest = 0
# most_common = ""

# for error in count:
#     if count[error] > highest:
#         highest = count[error]
#         most_common = error

# print("Most common error code:", most_common)
# output---> Most common error code: 404