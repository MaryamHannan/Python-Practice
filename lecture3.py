# list & tuples in python 
List=[2,1,3]
print(List.append(4))
print(List)

# print(List.sort())
print(List)
List.insert(1,9)
print(List)
#  tuple method 
tup=(1,4,5,7,5,3,3,3,2,6,7,3,3,7,3)
print(tup.index(3))
print(tup.count(3))
# print(tup)

# lets practice to append 3 movies in list
movies=[]
Movie1=(input("enter  name of  movie1"))
Movie2= (input("enter  name of  movie 2"))   
Movie3=(input("enter  name of  movie3"))
print(Movie1,Movie2,Movie3)
print(movies.append(Movie1))
print(movies.append(Movie2))
print(movies.append(Movie3))
print(movies)

#check if a list is palindrome or not (hint use copy method)
palindrome=[1,2,3,2,1]
pal2=palindrome.copy()
print(palindrome)
print(pal2)
print(pal2.reverse())
print(pal2)
if(pal2==palindrome):
    print("palindrome")
else:
    print("not a palindrome")
    # count A grade in tuple
    grades=('b','c','a','b','a','a','d','a')
    print(grades.count('a'))
    
    # create a list and sort them a to d 
    grade2=['b','c','a','b','a','a','d','a']
    grade2.sort()
    print(grade2)
