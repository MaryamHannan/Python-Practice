# delete keyword 
class Student:
    def __init__(self,name):
        self.name=name

s1=Student('Maryam')
# del s1
print(s1.name)
        #  private  
    
class Person:
    __name="anonymous"

    def __hello(self):
        print('hello person')

    def welcome(self):
        self.__hello()


p1=Person()
print(p1.welcome())

# Inheritance 
# single line inheritence 
# class Car:
#     @staticmethod
#     def start():
#         print('car started..')

#     @staticmethod
#     def Stop():
#         print('car stopped.')

# class Toyota(Car):
#     def __init__(self,name):
#         self.name=name

# car1=Toyota('fortuner')
# car2=Toyota('prius')

# print(car1.name)
# print(car1.start())
      

# Multilevel Inheritence 

class Car:
    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def Stop():
        print('car stopped.')

class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand


class Fortuner(Toyota):
    def __init__(self,type):
        self.type=type
        
car1=Fortuner('diesal')
car1.start()

# Multiple inheritance 
# eg

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
