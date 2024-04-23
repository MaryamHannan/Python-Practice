# Input/output in python 
# read mode 
# f=open('demo.txt','r')

# data=f.read()
# line1=f.readline()
# line2=f.readline()
# print(data)
# print(line1)
# print(data)
# print(line2)
# print(type(data))
# f.close()


# write mode ,append mode 
# f=open('demo.txt','a')
# f.write('\n this is a new line')
# f.close()


# read write mode 
# f=open('demo.txt','r+')
# f.write('abc')
# print(f.read())
# f.close()

# BY USING WITH KEYWORD 
# with open('demo.txt','r') as f:
#     data=f.read()
#     print(data)

# deleting a file 
# import os
# os.remove('sample.txt')

# practice q 1
# with open('sample.txt','w')as f:
#     f.write('Hi Everyone \n We are learning python')
#     f.write('using python\nI like programming in python')


# practice q 2
# relace python with java
# with open('sample.txt','r') as f:
#     data=f.read()

# new_data=data.replace('java','python')
# print(new_data)

# with open('sample.txt','w') as f:
#     f.write=new_data


# search the word 'learninig is available or not 
# word='learning'
# with open('sample.txt','r') as f:
#     data=f.read()

# if(data.find(word)!=-1):
#     print('found')
# else:   
#     print('not found')


# by using function search the word 'learninig is available or not 
# def check_word():
#     word='learning'
#     with open('sample.txt','r') as f:
#         data=f.read()

#         if(data.find(word)!=-1):
#             print('found')
#         else:   
#             print('not found')

# check_word()

# by using function search the word 'learninig is available at which line no

# def check_line():
#     word='learning'
#     data=True
#     line=1
  
#     with open ('demo.txt','r')as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line)
#                 return
#         else:
#             line+=1
#     return -1
    
# print(check_line())



# def check_line():
#     word='python'
#     line=1
#     with open ('demo.txt','r')as f:
#         data = f.readline()  
#         # read the first line
#         while data:
#             if(word in data):
#                 print(line)
#             line += 1
#             data = f.readline()  
#             # read the next line
        

#     print(check_line())

def check_line():
    word='python'  # specify the word to search for
    line=1         # initialize the line number
    found = False  # initialize the flag to track whether the word was found
    with open ('demo.txt','r')as f:   # open the file in read mode
        data = f.readline()   # read the first line
        # read the file line by line
        while data:
            if(word in data):   # if the word is found in the current line
                print(line)    # print the line number
                found = True  # set the flag to True
            line += 1          # increment the line number
            data = f.readline()   # read the next line

    if not found:
        print("Word not found.")

# call the function to search for the word in the file
check_line()



# q3 from a file containing numbers separated by commas
# print the count of even no

# to print all nos
# with open('sample.txt','r') as f:
#     data=f.read()
#     print(data)
#     num=''
#     for i in range(len(data)):
#         if(data[i]==','):
#             print(int(num))
#             num=''
#         else:
#             num+=data[i]


# solve by using method
count=0
with open('sample.txt','r')as f:
    data=f.read()
    nums=data.split(',')
    for val in nums:
        if (int(val)%2==0):
            count+=1


print(count)

