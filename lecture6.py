# function & recursion 
def cal_sum(a,b):
    s=a+b
    # print(s)
    return s

print(cal_sum(int(input("enter value1 ")),
              int(input('enter value2 '))))

def avg_no(a,b,c):
    
    return ("average of 3 no are",(a+b+c)/3)

ag=avg_no(3,6,9)
print(ag)
# Q1
# waf to print the length of ciies 
cities=['karachi','lahore','isl','mul','quetta']
def cal_cities(city):
    print(len(city))

print(cal_cities(cities))

# Q2
# waf to print the element of a list in 
# a single line (list is the parameter)
heroes=['ironman','thor','captain','ben10']
def cal_heroes(List):
    for item in List:
        print(item,end=" ")

    
print(cal_heroes(heroes))

# Q3
# waf to find factorial of n (n is pparameter)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("factorial is",fact)



def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial of a no is ", fact)

print(cal_fact(5))

# Q3
# waf to convert usd into pkr


def cal_rupee(no):
    con=277
    print("usd in pkr is",no*con)

print(cal_rupee(5))

# Q4
# waf to take input no and check odd or even 
def odd_even(num):
    if (num%2==0):
        print("this is a even no", num)
    else:
        print("this is odd no ",num)

print(odd_even(int(input('enter a num'))))

# Recursion 
# to show no 1 to 5
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

# calculate factorial 
def fact(n):
    if(n==0) or (n==1):
        return 1
    
    else:
        return fact(n-1)*n
    
print(fact(5))
# Qno1
# calculate the sum of 1st n natural no 

def cal_sum(n):
    if n==0 :
        return 0
    return cal_sum(n-1)+n

print(cal_sum(10))
# qno2
# to print all elements in a list 

def print_List2(List, ind=0):
    if(ind==len(List)):
        return
    print(List[ind])
    print_List2(List,ind+1)


hero=['ironman','thor','captain','ben10']

print_List2(hero)