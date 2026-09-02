# f=open("sample.txt","w")
# f.write("learn python")
# f.close()     //write


# f=open(r"C:\Users\swath\OneDrive\Desktop\Python\data.txt","w")
# f.close()   // add

# f=open("sample.txt","r")
# print(f.read())
# f.close()    // read    



# f=open("sample.txt","a")
# f.write("learn c\n ")
# f.close()   


# f=open("sample.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close() 


# f=open("sample.txt","r")
# print(f.readlines())
# f.close()    


# f=open("sample1.txt","x")
# f.close()    



# f=open("4.jpg","rb")
# print(f.read())
# print(f.read(10))
# f.close()


# f=open("sample.txt2","r+")
# print(f.read()) //FileNotFoundError:
    
    
# f=open("sample.txt","r+")
# print(f.read())//exist file use 


# f=open("sample.txt","r+")
# print(f.read())
# f.write("goodbye\n")
# print(f.read())
# f.close()


# f=open("sample.txt","r+")
# print(f.read())
# f.close()


# f=open("sample2.txt","w+")
# f.close() 

# f=open("sample1.txt","w+")
# print(f.read())
# f.write("goodbye\n")
# print(f.read())
# f.close()





# f=open("sample.txt","a+")
# print(f.read())
# f.write("goodbye\n")
# print(f.read())
# f.close()


# f=open("sample3.txt","w")
# f.write("welcome to python\n")
# print(f.name)
# print(f.mode)
# print(f.closed)
# f.close()
# print(f.closed)


# f=open("sample4.txt","w")
# f.writelines(['hello world\n','learn python \n','learn java \n','learn c++ \n','learn c \n','goodbye!\n'])
# f.close()   




with open("sample4.txt","w")as f:
    f.write("hello")