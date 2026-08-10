'''
Strings-->caseconversions,seraching&finding,string testing methods,replace,space removal
'''
'''
a="Codegnan"
print(len(a))
print(min(a))
print(max(a))
b=a.index('g')#it returns the index position
print(b)
c=a.index('n')#it returns only the first occurance
print(c)
d=a.index('n',6)#it returns the next occurance
print(d)
#e=a.index('n',8)#value error
#print(e)
#f=a.index('t')#value error
#print(f)
g=a.index('n',1,6)#gives index of the first occurance in that range
print(g)
'''


'''
#rindex () is used to return the last occurance
a="Codegnan"
b= a.rindex('g')
print(b)
c= a.rindex('n')#here n is occuring at the 7th postion last time
print(c)
d=a.rindex('n',8)#value error
print(d)
'''

'''
#count()-->returns the number of times object is repeating
print("Codegnan".count('n'))
print('Code'.count('w'))#it returns 0 as we dont have w in 'code'
print('VaishnaviJashnaviVidya'.count('a'))
'''

'''
#find()-->gives first occurance but it avoids error ,returns -1 if substring is not found
print("Codegnan".find('n'))
print("codegnan".find('r'))#returns -1
print("code".find('c'))
print("codegnan".rfind('n'))
'''

'''
a="DataAnalysis"
print(len(a))
for i in a:
    print(a.count(i))
b="Data"
for i in b:
    print(b.count(i),b.index(i))
'''

'''
#Replacing,Splitting,Joining
a='Codegan'
print(a.replace('g','s'))#just replaces doesnt change the string
print(a)
a=a.replace('g','s')#change the string and stores 
print(a)
print('fghjklpoiuyfcvbn#vklfghjk#fghj'.replace('#',''))#replace with empty space
print('Vaishnavi'.replace('V','J'))
'''


'''
a='vaishnavi jashnavi vidya'
print(len(a))
b=a.split()
print(b)
print(len(b))
c=a.split(',')#doesnt split because ',' is not there in input
print(c)
'''



'''
#join(iterable)-->concatenate any number of strings
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('Vaishnavi'))
print(' '.join('vaishnavi'))
'''


'''
#String Testing Methods(boolean)-->isalpha(),isnum(),isdigit(),isupper(),islower()
a='Codegnan12'
print(a.isalnum())#returns true for alphanumeric strings else false
b='codegnan'
print(b.isalnum())
print(b.isalpha())#returns true only for alphabets
print(b.isdigit())#returns true only for digit string
print('9381752623'.isdigit())
print('2345'.isnumeric())#this has upper edge (numbers,fractions,romans)
print('codegnan'.startswith('c'))#startswith() shows howits starting
print('codegnan'.startswith('g',4))#starts counting from g as 4 is mentioned
print('codegnan'.endswith('g'))
print('codegnan'.islower())#returns true for all lower cases
print('COdegnan'.isupper())#returns true for all upper cases
print('Codeganan Python'.istitle())
'''


'''
#Space removal-->strip()removes leading and trailing spaces
a=' codegnan  '
print(a.strip())
b=input('enter the string:').strip().lower()
print(b)
'''


#zfill()-->filling with zeros asper the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))
#center(),ljust(),rjust()-->alignment of strings (check length and then modify the width accordingly
print('hai'.center(6))
print('hai'.center(6,'#'))
print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))
