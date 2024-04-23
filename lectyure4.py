info={
    "key" :"value",
    "name" :"maryam",
    "learning":"coding",
    "age":22,
    "it's adult" : True,
    "course" : ["python","c","powerbi","stats"],
    "topic" :('dict','set')
}
print(info)

# bested dictionary 
stu={
    'name':'maryam',
    'courses' :{
        'python' :78,
        'c': 74,
        'java': 60

    }
}
print(list(stu.keys()))
print(len(stu.keys()))

# Sets in python 
collection={1,2,3,4,'hello','world'}
print(collection)
print(type(collection)) 
collection={'hello',1,2,2,3,2,3,4,'hello','world'}
print(len(collection)) 
print(collection)
# create empty set
coll=set()
print(type(coll))
coll.add(1)
coll.add(2)
coll.add('apnaCollege')
coll.add((1,2,3,3))
print(coll)

# delete random value
collect={'hello','apna','coding','python'}
collect.pop()
print(collect)
# union & intersection
set1={1,2,3,4,5}
set2={2,4,6,8,10}
print(set1.union(set2))
print(set1.intersection(set2))

# lets practice q1 
# store word meaning in python dictionary 
store={
    'table':('a piece of furniture','list of fact & figures'),
    'cat':'a small animal'
}
print(store)

# lets practice q2
# you are given a list of subject for student .Assume one classroom 
# is required for 1 subject.How many classroom are needed by all student
# 'python','java','C++','python','javascript'
# ,'java','python','java','C++','C' 
subj={'python','java','C++','python','javascript',
'java','python','java','C++','C' }
print(subj)
print(len(subj))

# lets practice q3 
# input 3 sujects marks in dict. use empty dict and store 1 by 1.
# use subj name as key and marks as value

subject={}
subj1=int(input("enter marks of subj1 "))
subject.update({'subj1':subj1})
subj2=int(input("enter marks of subj2 "))
subject.update({'subj2':subj2})
subj3=int(input("enter marks of subj3 "))
subject.update({'subj3':subj3})
print(subject)

#figout a way to store 9 & 9.0 as separate values in set
# (you can use build in data type)
storfloatint={9,'9.0'}
print(storfloatint)
#  2nd sol 
values={
    ('float',9.0),
    ('int',9)
}
print(values)