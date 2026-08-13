'''
Sequences-->Strings,Lists,Tuples,Sets
Mapping-->Dictionary

#Lists-->Collection of hetrogenous elements or items
Lists are indexed,ordered,mutable,hetrogenous,we use[] to store the data


marks=[32,45,21,43]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)

#Operations:Indexing,Slicing,Striding,Membership,Repetition
'''


'''
#Nested Lists--> a list inside another list
names=['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4])#it returs code from codegnan
print(names[0][4:])
print(names[0][::2])#to get output as cdga
names[0]=names[0][::-1]#gives reverse ogf codegnan
print(names)
'''



'''
names=['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names)
print(names[3])
print(len(names[3]))
print(names[3][2])
names[2]='Python' #replacing the values in list(len remains same)
print(names)
names[4]=['codegnan','da','ds',35] #replacing the data in list(len remains same)
print(names)
print(len(names))
print(names[4][1:4])
print(names[4][0][4:])#slices codegnan into gnan
'''

'''
names=['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
names[2:4]='Vaishnavi','Vidya','Jashnavi','Harshitha'
print(names)#replaces the data in list ,len changes
#In slicing slicing  whatever elements you pass as per the logic length keeps on increasing
names[3:6:2]='Python','Java'
print(names)
'''

#Create a nested list with strings,lists and work on indexing,slicing,striding,added advantage if you could add string functions also to it



#List functions-->append(),insert(),extend(),pop(),remove(),clear(),index(),count(),copy(),sort(),reverse()
names=['codegnan','saketh']
names.append('data')#append inserts single element to the end of the list
print(names)
names.append(['analysis','agents'])
print(names)#append will always increment the length of list by 1
print(names[3])
names[3].append('chatgpt')
print(names)
print(names[3].append('chatgpt'))#returns none as append is applicaple on list not print
print(names[3])



'''
#extend()-->inserts multiple elements to the end of list
names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,45,78,89])
print(names)
#names.extend(35,45)Type error -->as only 1 argument to be passed
#print(names)
'''

'''
#insert(index,object)-->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b'])#Syntax error
#print(names)
names.insert(-1,'AAA')
print(names)
'''

'''
#pop(),remove(),clear()
#pop() by default last else given index(removes items from list)
print(names)
print(names.pop())#removes last item
print(names)
names.pop(2)
print(names)
'''

'''
#remove-->removes a specific value
names.extend([23,45,67])
print(names)
names.remove(45)
print(names)
#names.remove(14)-->gives value error
del names[1:3]#del keyword will apply permanent changes
print(names)
names.clear()#clear() will remove all the elements and returns empty list
print(names)
'''
'''
#Task: Input:data=['codegnan','saketh','pythom','java']
#Output should be as follows
0:codegnan
1:saketh
2:python
3:java
'''

data=['codegnan','saketh','python','java']
for i in data:
    print(f'{data.index(i)}:{i}')
