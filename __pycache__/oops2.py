# polymorphism 
# class Dog:
#     def speak(self):
#         print("woof")
# class Cat:
#     def speak(self):
#         print("meow")
# animals = [Dog(),Cat()]
# for a in animals:
#     a.speak()  



# class Car:
#     def moving(self):
#         print("Car is moving on road")


# class Boat:
#     def moving(self):
#         print("Boat is moving on water")


# class Plane:
#     def moving(self):
#         print("Plane is flying in the sky")


# car = Car()
# boat = Boat()
# plane = Plane()

# vehicle = [car, boat, plane]

# for v in vehicle:
#     v.moving()  



# class File:
#     def read(self):
#         print("reading file")
# class Socket:
#     def read (self):
#         print("reading socket")
        
# def fetch_data(source):
#     source.read()
# fetch_data(File())
# fetch_data(Socket())  




# class student:
#     def __init__(self):
#         self._marks=0
#     @property
#     def marks(self):
#         return self._marks
#     @marks.setter
#     def marks(self, value):
#         if value < 0:
#             print("invalid marks")
#         else:
#             self._marks =value
# s=student()
# s.marks =80
# print(s.marks)  

# encapsulation 

# class Student:
#     def __init__(self):
#         self.__marks = 80
#     def  show_marks(self):
#         print(self.__marks)
# s = Student()
# s.show_marks() 


# encapulation
# class Student:
#     def __init__(self):
#         self.__marks = 80
#     def  get_marks(self):
#        return self.__marks
#     def set_marks(self,value):
#          self.__marks = value
# s = Student()
# print(s.get_marks())
# s.set_marks(100)
# print(s.get_marks())  