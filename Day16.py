'''
Exception Handling/Scope of variables/Built-in functions
Exception handling-->it is a mechanism that helps torespond or make the flow of execution in normal way, without this errors will occur and disrupt the flow of program
It occurs at runtime and logical mistakes
Common Exceptions-->ValueError,TypeError,IndexError,AttributeError,ZeroDivisionError

Syntax:

try:
    #code that will cause the exception
except Exception as e:
     #code will catch the exception
finally:
      #runs irrespective of try/except...
'''



'''
#basic Exception Handling
try:
    #a=10
    a=int(input("enter the value:"))
    l=list(map(int,input("enter the values").split(','))
    result=20/a
    print(result)
#except Exception as e:
    #print(e)#it returns the msg of error
except ValueError:
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'devision by zero')
except NameError:
    print(f'check the name of the variable properly')#example:result is given as resul (being incomplete or different spelling)
'''


'''
#Similarly if we want to check other errors-->IndexError,AttributeError
try:
    a=[10,20,30]
    a.append(24)
    print(a[3])
#except Exception as e:
    #print(e)
except IndexError:
    print("check the length of the list properly")
except AttributeError:
    print("dont rush write the name properly")#spelling mistakes of attributes like(append-->appen)
'''


'''
#Multiple Exception Handling
try:
    a=[10,20,30]
    a.appen(24)
    print(a[5])
except (IndexError,AttributeError)as e:
    print(e)
'''


'''
#BMI-->bmi=(weight)/((height)**2)
#Feet-->12 inches , 1inch-->2.54cm
while True:
    try:
        weight=int(input("enter the weight in kgs:"))
        height=int(input("enter the height in metres:"))
        if weight>0 and height>0:
            break #stops the flow of execution of program
            #continue #skips the current iteration and proceed for remaining items
            #print("bye")
        else:
            print("Make sure to enter only correct values")
    except ValueError:
        print(f'Make sure to enter weight as integer only,height also as number')
bmi=(weight)/((height)**2)
print(bmi)
'''

'''
use exception handling along with jumping statements in functions bmi task


Scope of variables --> Scope is basically the region/area where it is accessible
Local Scope, Global Scope
Local Scope --> variables defined inside the function accessible inside 
Global keyword,Enclosing Scope(Nested functions non local Keyword)
'''

'''
def display():
    """Usage of local Scope"""
    name="Codegnan"#local variable
    print(name)
display()
#print(name)#it raises name error
'''


'''
#Global Scope(variables)-->defined outside and can be accessible anywhere in the scriptt
place="Hyderabad"#global variable
def display():
    """Usage of Local&Global Scope"""
    name="Codegnan"#local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)
'''


'''
#Modfying global variable inside the function and accessible outside the function
count=20
def data():
    """Usage of global keyword"""
    global count#if we dont use global inside function count is not recognised and get Unboundlocal Error
    count=count+5
    print(f'value inside function is {count}')
data()
print(f'Value outside function is {count}')
'''

'''
#Enclosing Scope (non-local keyword)
def outer():
    """Outer function with local variable"""
    count=5
    def inner():
        """Nested Function"""
        nonlocal count
        count=count+10
        print(f'Value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()
'''

#Built-in-functionss-->variables BuiltinScope
len=56
print(len+4)
#print(len('Codegnan'))#TypeError-->never use b

