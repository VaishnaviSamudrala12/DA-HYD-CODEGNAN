'''
#Identity operators
a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#as we have lists (Mutable collection)both c and a lists will have different ids whereas values are same
print(c is a)#output False
print(c == a)#output True
print(c is not a)
'''


'''
#Bitwise operartors-->we perform bitwise operations over operands{&(and),|(or),^(XOR),shifting operators(<<,>>)}
print(5&3)#both 5 and 3 to be converted binary and bitwise and is performed
print(5|3)#bitwise OR
print(5^3)#bitwise XOR
print(5 and 3)#here and is logical operator checks for both existances,returns 3 in this case
print(5 or 3)#returns 5 in this case
'''


'''
#leftshift operator(<<),Rightshift operartor(>>)
print(5<1)#false comparision
print(5<<1)#leftshift to one position
print(5>>1)
print(15<<2)#convert 15 to binary and perform 2 times shifting
print(15>>2)#same 2 times right shifting
print(5>>4)
'''



#Tokens-->numeric datatypes--.operators-->flow of program
#Control block statements-->they control the flow of the program,tellswhen and how to execute
#Conditional Statements-->if,else,elif 9rely on condition to be executed)
#Repetitio Statement(Loops)-->for,while

#Conditional Statements-->if usage
'''
Syntax:
if <condition>
    statement(s)...
    ....
'''
'''
age=int(input("enter the age:"))
if age>15:
    print('your age is:',age)
'''
'''
age = int(input("enter the age:"))
if age>18 and age in[18,20,16]:
    print("your age is:",age)
'''



#Conditional Statements-->else keyword-->if-else(onle else is not written it is written with if)
'''
Syntax:
else:
     statement(s)...
     ...
'''

'''
if-else usage as below:
if <condition>
    statement(s)...
else:
     statement(s)...
'''
'''
#Vote eligibility-->to check his/her voter eligibility and give access
age=int(input("enter your age:"))
if age>=18:
    print("you have voter eligibility and age is",age)
    print("access granted")
else:
    age=18-age
    #print("you dont have eligibility as your age is ",age)
    print("you need to wait for more",age,"years")
'''
'''
#Same case lets use only nested-->if,else
age=int(input("enter your age:"))
if age>0:
    if age>=18:
        print("you have voter eligibility and age is",age)
        print("access granted")
    else:
        age=18-age
    #print("you dont have eligibility as your age is ",age)
        print("you need to wait for more",age,"years")
else:
    print("you have entered -ve values/zero enter only +ve")
'''
'''
task:students marks and grade analyzes
90-100-->A
80-89-->B
70-79-->C
60-69-->D
<60-->Fail
#also -ve negative cases should not be allowed and marks should not be greater than 100
    
    
