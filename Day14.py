'''
FUNCTIONS--.a function is a block of code which performs a specific task
Its a reusable group of statements where we define using def keyword
Advantages-->code reuseability,code maintainability,ease of debugging,avoiding code duplication,modularity

def fname(parameters):#Function defination
    """Doc String"""
    statement(s)....#Function body
    .......
    return value(s)....
fname(args) #Function call
'''


'''
#To perform sum of given objects
def add(a,b):
    """Sum of objects"""
    c=a+b
    return c
print(add(12,3))#adding
print(add('code','gnan'))#concatination
print(add([12,5],[12,34]))#merging
c,d=map(int,input("enter the values:").split(','))
print(c,d)
print(add(c,d))


def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34))#it returns result along with None



name,age,salary='Saketh',32,50000
#usage of return

def details():
    return name,age,salary
print(details())
'''


'''
There are 5 types of arguments:
-->Positional arguments
-->Default arguments
-->Keyword arguments
-->Variable length arguments(*args)
-->Keyword variable length arguments(**kwargs)

POSITIONAL ARGUMENTS:number of arguments in function defn should match with function call (order has to be maintained)
'''
'''
def details(name,place):
    """to store the details"""
    #name="codegnan"
    #place="hyderabad"
    #return name,place
    print(f'Name is {name}')
    print(f'Place is {place}')   
#print(details("saketh","codegnan"))
#print(details("sai","vizag"))
#print(details("vizag","shyam",34))#raises type error as only two arguments to be passed
c,d=map(str,input("enter the values:").split(','))
details(c,d)
'''


'''
#Default arguments-->we can make arguments as default but not first arument as default
def grocery(item="cheese",price=35):#we can also make all args as default
#def grocery(item='Burger',price)#non default always follows default
    """usage of default arguments"""
    print(f'the item is {item} and price is {price}')
grocery("Milk",32)
grocery("Bread")#by default we have given price as 35
grocery("Bread",45)
grocery()#by default item and price are given
'''


#Keyword arguments-->whenever we want tospecify the name of argument
def employee(name,salary,role,place="codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary}\works in {place}')
employee("sai",20000,"admin")
employee(salary=25000,role="frontdesk",name="Asha")
employee("Akash",25000,"IT","Codegnan")
    
