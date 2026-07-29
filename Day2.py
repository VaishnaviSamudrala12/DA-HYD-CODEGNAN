'''
#multiassignmentof variables
name,age,place="vaishnavi",21,"hyderabad"
print(name,age,place)
print(name,age,place,sep=',')#used to seperate data using comas
print(name,age,place,sep=';')#sep is used to seperate data using symbols
'''



'''
#reassigning variables
a,b=2,3
print(a,b)
a,b=b,a #swapping of variables is done here just by changing 
print(a,b,sep=',')

#deleting the variables (done using del kayword)
del a,b
print(a,b)
'''



'''
#punctators --->[](used for lists),()(used for tuples),{}(used for dict,sets)
name='codegnan';age=7 #this is how and where semi colon is used to give multiple variables in same line
print(name,age)
'''



#Datatypes
#Numeric(int,float,complex),boolean,None
#Sequences(lists,tuples,sets,strings,frozensets,mapping(dict)

'''
#int datatype --->quantity,age...
age=7
print(age)
print(type(age)) #type is used to show the datatype of object
print(type(456))
#quantity=03 it is not allowed
#print(quantity)
'''


'''
#float datatype --->tempurature,salary,price
price=750.24;discount=2.5
print(price,discount,sep=',')
print(type(price))
'''


'''
#complex datatype --->combination of real and imaginary
data=5+2i #i is used for other purposes so j is taken for complex notation or j is imaginary representation 
print(data)
'''


'''
data=2+5j
print(data)
print(type(data))
'''



'''
#Boolean datatype --->True/False
valid=True
print(type(valid))
print(valid)
error=False
print(type(error))
print(error)
'''


#Typecasting --> Converting one type to another type
#python is by default follows implicitbtypewe dont need to mention datatype
#we will go for explicit conversion
#every built-in datatype is a built in function in python
'''
#Typecasting---> int to float,complex,boolean
age=35
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e)
'''


'''
#Typecasting--->float to int,complex,bool
age=35.23
print(type(age))
b=int(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e)
'''

'''
#myexample
price=680.90
print(type(price))
b=int(price)
print(b)
c=complex(price)
print(c)
d=bool(price)
print(d)
'''

'''
#Typecasting--->complex to int,float,bool  (complex cannot convert,but can only conert into boolean)
img=2+6j
print(type(img))
b=int(img)
print(b)
c=float(img)
print(c)
img=2+6j
d=bool(img)
print(d)
'''


'''
e=int(float(bool(45)))#first bool of 45 is true,next float of true is 1.0,then int of 1.0 is 1
print(e)
b=bool(int(float(25)))
print(b)
'''


'''
#arithemetic operation
f=45+2.5+2+3j+False #(Here anything +0 is the same value nothing chnages as false is a 0 so answer is 49.5+3j)
print(f)
'''
