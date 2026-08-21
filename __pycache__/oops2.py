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



class File:
    def read(self):
        print("reading file")
class Socket:
    def read (self):
        print("reading socket")
        
def fetch_data(source):
    source.read()
fetch_data(File())
fetch_data(Socket()) 