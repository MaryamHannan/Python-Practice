# class Student:
#     name='karan'

# s1=Student()
# print(s1.name)

# class Factory:
#     car="blue"
#     brand='mercedes'


# b=Factory()
# print(Factory.car)
# print(Factory.brand)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student in db")

#     def welcome(self):
#         print('welcome student',self.name)

# s1=Student('karan',65)
# s1.welcome()
# print(s1.name,s1.marks)


# s2=Student('arjun',78)
# print(s2.name,s2.marks)



     # practice q 1
# create student class that takes name & marks of 3 
# subject as arguments in constructor. then create 
# a method to print avg
# class Student:
    # name="maryam"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def cal_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val

#         print('hi',self.name,'your avg score is ',sum/3)
        
        

# s1=Student('ali',[98,53,25])
# s1.cal_avg()

# static method 

class Student:
    # name="maryam"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print('hello')

    def cal_avg(self):
        sum=0
        for val in self.marks:
            sum+=val

        print('hi',self.name,'your avg score is ',sum/3)
        
        

s1=Student('ali',[98,53,25])
s1.cal_avg()


class Car:
    def __init__(self) :
        self.accelerator=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.accelerator=True
        print('car started.. ')


car1=Car()
car1.start()
# lets practice
# create account class with 2 attributes balance &
# account no .create method for debit & credit & printing the 
# balance

class Account:
    def __init__(self,account_no,bal) :
        self.bal=bal
        self.acc=account_no
   


    def debit(self,amount):
        self.bal-=amount
        print('Rs',amount,"was debited")
        print('total balance=',self.get_balance())

    def credit(self,amount):
        self.bal+=amount
        print('Rs',amount,'was credited')
        print('Total balance =',self.get_balance())

    def get_balance(self):
        return self.bal
    
acc1=Account(10000,12345)
print(acc1.bal,acc1.acc)
acc1.debit(1000)
acc1.credit(500)


