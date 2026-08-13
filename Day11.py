'''
#Lists,Tuples
#List-->mutable,ordered.hetrogenous:index(),count(),copy(),sort(),reverse()
'''

'''
details=['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))
print(details.index(21,6))#returns position of 21 after 6th index
#print(details.index('python'))#value error
print(details.count(21))
print(details.count('python'))#it returns 0 as we dont have it
'''

'''
#copy()
data=['codegnan',7,2018,'Hyderabad']
new =data.copy()
print(new)
print(type(new))
print(len(data))
new[2]='Agentic AI'
print(new)
print(data)
data.append('saketh')
print(data)
print(new)
'''

'''
data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)
new[3][2]='Agents'#nested lists can change the data in original list also
print(new)
print(data)
new[1]='Python'#doesnt change the original list if not used nested list
print(new)
print(data)
'''


'''
#Sort() and Reverse()
marks=[14,24,-45,27,35]
print(marks)
#print(marks.sort())#returns None
marks.sort()
print(marks)#returns ascending order
marks.sort(reverse=True)#returns descending order or returns in reverse order
print(marks)
marks.insert(2,'code')
print(marks.sort())#returns error as string is given
marks.reverse()
print(marks)
print(marks[::-1])

#type(),len(),max(),min(),print()
print(sorted('codegnan'))#returns list in ascending order
#print(sorted(['code',34,56,78]))#raises error
'''

'''
#Tuples-->Tuples are Indexed,ordered,hetrogenous,immutable,collection(used for dimensons,coordinates,database,records,we prefer() for tuple notation
a=()
print(type(a))
print(len(a))

dimensions=1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))

#Operations-->Indexing,slicing,striding,membership,merging,repetition
courses=('PFS','JFS',('DA','DS'),'AgentAI',[100,6,6])
print(courses)
print(len(courses))
print(courses[3][-2:])
#courses[2]=23 #tuples are immutable
courses[-1].append('codegnan')#we can make any changes inside the list that doesnt effect the tuple
print(courses)

#Task:create a nested tuple as above and work on slicing and striding and list functions
print('PFS' in courses)#returns true
d=courses*2#repetitive
print(d)
e=courses+(2,3,4,5)#merging
print(e)

#Tuples are immutable  ,can only performs count(),index()
print(courses.index('AgentAI'))
print(courses.count('Agents'))
#print(courses.sort())3attribute error--> sort() can be used in lists not in tuples
#print(sorted(courses[-1]))
#print(sorted(courses))#as we have mixed type

#TypeCasting
d=tuple(sorted((23,12,3,4,5)))
print(d)
'''

'''
#accept group of integers space seperated
a,b=map(int,input("enter values:").split())
print(a,b)
a=tuple(map(int,input("enter values:").split(',')))
print(a)

#eval() function can take any kind of input
a=eval(input("enter a list:"))
print(a)
print(type(a))
'''

'''
Task:take a user input as string,do thisin two ways
1) give the countof each repeating character
Test case 1:programming
r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)r is repeating 2 times
index=[1,4]
g is repeating 2 times
index[3,10]
m is repeating 2 times
index=[6,7]
'''
