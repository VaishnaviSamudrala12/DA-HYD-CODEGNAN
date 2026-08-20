'''
Functions-->Variable length arguments(*args)
         -->Keyword Variable length arguments(**kwargs)
Variable length arguments-->the number of positional arguments are not limited we can pass any number of arguments ,but we need to use the * representation,data is stored in tuple
'''

'''
def sample(*args):
    """Simple demo for *args"""
    print(args)
    print(type(args))
sample()#no arguments
sample(1,3,5,6)#any number
sample('codegnan','saketh',23)
details=[24,45,35,65]
sample(details)#returs list inside tuple as length 1 (passing a collection)
sample(*details)#returns details inside a tuple as length 4 (unpacking a collection)
'''

'''
a,b,c=13,4,'da'
print(a,b,c)
#a,*b,c='python','codegnan',23,45,9.7,'data'
#a,b,*c='python','codegnan',23,45,9.7,'data' #used to unpack values
a,b,*c='code','gnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)
'''


'''
#Task-->we wanted to calculate the sum of given objects using functions
def add(*a):
    """Sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result=0
    for i in a:
        #print(i)
        if type(i)==int or type(i)==float:
            #print(i)
            result=result+i
    return result
            
            
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,.5))
#print(add(3,4,5,4.5,'poll','dear',45))
b=list(map(int,input("Enter the values:").split(',')))
print(add(*b))#(*) is used to unpack the values from collection
#print(*b)#it returns each value side by side
#for i in b:
    #print(i,end=' ')#it also returns each value side by side
'''




'''
Keyword variable length arguments--> we can pass any number of keyword arguments,we use ** for representation
Datais stored in dictionary
'''

'''
def details(**kwargs):
    """Usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()#returns empty dictionary
#details(2,3,4,5,6)#raises type error
details(name="codegnan",place="hyd",batch="da")
batch={'number':'da23','place':'hyd'}
details(**batch)
details(**batch)
'''


#Now let us include both of them into a function
def sample(*a,**b):
    """Usage of both variable length and keyword variable length args"""
    result=0
    for i in a:
        if type(i) in(int,float,complex):
            result=result+i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
    return result
sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch="da23")
#sample(name='codegnan',23,ids=2345)#positional args follows keyword args
