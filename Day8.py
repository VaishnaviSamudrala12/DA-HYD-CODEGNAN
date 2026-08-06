'''
SEQUENCES-->strings,lists,sets,tuples,mapping(dict)
#STRINGS-->are group of characters,we use single or double or triple quotes for representation of strings
strings are immutable,ordered,indexed collection
space is also a character in strings 
'''

'''
name="codegnan"
print(name)
print(type(name))
print(len(name))#len-->returns the no of items in container



#index()-->fetch the object(position),starts at 0 and ends at len(obj)-1,we use[] for representation
name="codegnan"
print(name[0])#returns index
print(name[5])
#print(name[25])#raises index error as it is out of range
#Negative indexing-->-1 to len(obj)
print(name[-1])
print(name[-3])
print(name[-33])#index error
'''


'''
#SLICING-->we can access group of characters(objects)
we use [start:end] -->start is default as 0,and end is excluded-->(len-1)
Slicing is applicable from lower index to higher index and not possible from higher to lower



name="codegnan"
print(name[:])#returns entire string
print(name[0:])#returns entire string
print(name[:4])#starts at 0th index and ends before 4th index
print(name[1:5])
print(name[:5])
print(name[7:3])#returns empty as strings are immutable
print(name[:45])#returns till the end of the string



name="Python"
print(name[-3:-5])#returns empty string
print(name[-5:-1])#startsat -5 and ends at -2
print(name[4:6])
print(name[-2:])
print(name[1:-2])
print(name[2:-6])#returns empty string as it cannot perform slicing
'''


'''
#STRIDING-->[start:end:step]
course="DataAnalysis"
print(course[:4])
print(course[4:])
print(course[-3:])
print(course[::1])#returns all characters
print(course[::2])#skips one letter between each letter,here step=2 that means gap is 1
print(course[1:6:3])#[1:6]-->ataAn-->aA
print(course[2:12:3])
print(course[::-1])#it returns the reverse of a string
print(course[::-2])

#TASK:workout with all possibilities of slicing and striding on a example
name="codegnan"
name[3]='w'#strings are immutable so we cannot change e to w
'''

'''
#Operations on strings-->Indexing,Concatination,Repetition
#REPETITION
name="codegnan"
print(name*3)
print('*'*25)


#CONCATINATION
data= "vaishnavi"+"dataanalysis"+' '+"codegnan"
print(data)
print('123'*4)
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')#in this case we get every character line by line

name="codegan"
for i in 'codegnan':
    print(i,end=' ')

name='vaishnavi'
for i in name:
    print(i)
'''



#Buit-in-functions-->len(),min(),max(),sorted()
name="Codeganan"
print(len(name))
print(min(name))#alphabetical order ASCII ordering
print(ord('A'))#to know the order of A in ASCII(value of letter in ASCII)
print(ord('a'))
print(chr(97))#gives ASCII letter
print(max(name))
print(sorted(name))#returns a list by sorting all elements



'''
#Methods on strings-->Case-conversion,Finding/Searching...
CASE-CONVERSION-->upper(),lower(),title(),capitalize()
'''
'''
name="codEgnan data"
a=name.upper()#conerts to upper case
print(a)
b=name.lower()
print(b)#upper to lower
#Capitalize()-->conerts first letter to upper
c=name.capitalize()
print(c)
d=name.title()
print(d)
'''
#TASK:A-Z
#USE LOOPS and strings to return A-Z
for alphabets in range(65,91):
    print(chr(alphabets),end=" ")

