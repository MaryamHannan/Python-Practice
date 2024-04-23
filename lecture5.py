# while loop 
count=1
while count <= 5 :
    print('hello')
    count+=1

    # print no from 1 to 100 
    no=1
    while no<=100:
        print(no)
        no+=1
     # print no from 100 to 1 
nos=100
while nos >= 1:
    print(nos)
    nos-=1

   # print multy of a no n
num=int(input('enter no'))
count=1
while count<=10:
    print(num*count )
    count+=1

    # print the elements of following list using a loop 
    # [1,4,9,16,25,36,49,64,91,100]
Listno=[]
# squareno= [1,4,9,16,25,36,49,64,91,100]
sqno=1
while sqno<=10:
      
    Listno.append(sqno*sqno)
    sqno+=1
print(Listno)

# 2bd method 
# squaresno= [1,4,9,16,25,36,49,64,91,100]
# it=0
# while it<= len(squaresno):

#     print(squaresno[it])
#     it+=1



#  q5 search for a no x in this  tuple using loop  
    # (1,4,9,16,25,36,49,64,91,100)

# numbers=(1,4,9,16,25,36,49,64,91,100,36)
# x=36
# i=0
# while i<=len(numbers):
#     if(numbers[i]==x):
#       print("found at index",i)
#     else:
#         print('finding')
#     i+=1
    
    # break & continue 
iter=1
while iter<=5:
    print(iter)
    if(iter==3):
        break
    iter+=1
print("end of loop")


# use of break keyword 
# numbers=(1,4,9,16,25,36,49,64,91,100,36)
# x=36
# i=0
# while i<=len(numbers):
#     if(numbers[i]== x ):
#       print("found at index",i)
#       break
#     else:
#         print('finding')
#     i+=1
# print("end of loop")

# use of continue keyword 
# iter=1
# while iter<=5:
#     print(iter)
#     if(iter==3): 
#         continue
#     iter+=1
# print("end of loop")



# for loop 
nums=[1,2,3,4,5]
for val in nums:
    print (val)
else:
    print('end')

# eg2 
str="apnacollege"
for char in str:
    if(char=='o'):
        print('o found')
        break
    print(char)
else:
    print('end')

# practice q2 for loop
# print the element using for loop 
ele=[1,4,9,16,25,36,49,64,81]
for y in ele:
    print(y)

# search for a no x in this tuple using for loop 
sear=(1,4,9,16,25,36,49,64,16,56,26,16,16,12,16)
x=16
for el in sear:
    if(el==x):
        print("found",el)
    else:
        print('finding')
    
# range 
seq=range(5)
for z in seq:
    print(z)

for q in range(2,10): #(start,stop)
    print(q)


for xy in range(1,100,2): #(start,stop,step)
    print(xy)

# practice qs 
# print no from 100 to 1
for wa in range(100,0,-1):
    print(wa)

# print the multiplication of table n 
n=int(input("enter no"))
for i in range(1,11):
    print(n*i)

# pass statement 
# for i in range(5):
#     pass

# find the sum of 1st 10 nos using while loop 
ny=7
sum=0
iq=1
while iq<=ny:
    sum+=iq
    iq+=1
print('total sum=',sum)


# find factorial of first n numbers
fn=6
fact=1
i=1
while i<=fn:
    fact*=i
    i+=1
print("total fact",fact)



# find factorial of first n numbers
nt=5
facto=1
for j in range(1,nt+1):
    facto*=j
    j+=1
print('facto =' ,facto)
