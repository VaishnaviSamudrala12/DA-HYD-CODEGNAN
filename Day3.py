'''
#Numeric datatype --> int,float,complex along with boolean
#Input Formatting -->Accepting input from the user -->input()
#Accepting integer input from user
#int(input()) --> will accept only integers
age=int(input('enter the age:'))
print(age)
print(type(age))

#float(input()) will accept integer,float values
age=float(input('enter the age:'))
print(age)
print(type(age))

#Accepting string input from user
name=input("enter the name")
print(name)
print(type(name))
'''


'''
#comma seperated values
a=input("enter the values:").split(',')#split() is used to give multiple inputs at a time,by default split() has space
print(a)
#space seperated values
a=input("enter the values").split()#now you enter spaces in output
print(a)
'''


'''
#list of integers
marks=list(map(int,input("enter the values").split(',')))#map is used to give multiple integers and list is used to show the values to us 
print(marks)

#Now we want to accept 2 values from user
age,salary=map(int,input("enter the values").split(','))
print(age)
print(salary)
'''

#Single input-->int(input())
#two inputs-->a,b=map(int,input("enter the values").split(','))
#any number result as list-->list(map(int,input("enter the values").split(',')))

'''
age,salary=map(float,input("enter the values").split(','))
print(age)
print(salary)
marks=list(map(float,input("enter the values").split(',')))
print(marks)
'''


'''
price,discount=map(float,input("enter the values").split(','))
print(price)
print(discount)
price=list(map(float,input("enter the values").split(',')))
print(price)
'''


'''
#accepting input from user-->int,float-->input formatting

#OPERATORS-->operators perform operations between values(operands)
#7 types-->Arithmetic,assignment,comparision(relationship),membership,identity,logical,
#bitwise

#Arithmetic Operators-->arithmetic operations(+,-,*,/)
print(5+2)
print(7-2)
print(3*5)
print(5/6)
print(5//3)#floor division or integer divison ,this gives quotient
print(5%3)#modulus,it gives remainder
print(5**3)#power or exponential,this means 5 power 3 here
'''

'''
length=int(input('enter length:'))
breadth=int(input('enter breadth:'))
area=length*breadth
print(area)
'''

'''
length,breadth=map(int,input('enter the values:').split(','))
area=length*breadth
print(area)
'''


'''
#Assignment operators--> assign the values(=,+=,-=,*=,/=,//=,**=)
a=45
print(a)
#update the value of a
a+=5#a=a+5
print(a)
b=35
b+=a#b=b+a
print(b)
b-=5
print(b)
a*=3
print(a)
a/=6
print(a)
a//=4
print(a)
a**=2
print(a)
'''


'''
#Comparison operartos-->we compare the values,the output will be boolean(==,!=,<,>,<=,>=)
#(equal to,not equal to,less than,greater than,less than or equal to,greater than or equal to)
age=25
print(age==25)
print(age!=35)
print(age<20)
print(age>16)
print(age<=25)
print(age>=16)
print(-5<-2)
'''


'''
#Membership operators-->(in,not in),output will be in boolean
#it checks for existence of an object in a collection
marks=[23,34,56,67]#check whether the number is in list or not
print(34 in marks)
print(56 not in marks)
print(67 in marks)
print(45 not in marks)
print('code' in 'codegnan')#check the string is in the word or not
print('$' in 'abc$frg')
'''


'''
#Logical operators-->logical decision making(and,or,not)
#and-->all conditions to be satisfied
#or-->any one condition to be satsfied
a=(25 in[12,25,13])and 45>25
print(a)
b=45>25 or 25<=45
print(b)
c=not(True)
print(c)
'''


'''
#Identity Operators-->checks for identity of an object,uses id()
# is,is not
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)

a=[1,2,3,4,5]
print(id(a))
c=a
print(id(c))
print(c is a)
'''
