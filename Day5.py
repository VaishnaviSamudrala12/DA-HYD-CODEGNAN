#elif keyword(always comes with if)
'''
Syntax:
if<condition1>:
   statement(s)
elif<condition2>:
   statement(s)
elif<condition3>:
   statement(s)...
else:
    statements
'''
#Task-->same usecase as yesterday try with if-elif-else in other way

'''
#Voter eligibility checkcase-->make sure to satisfy all possible conditions
>=18-->access
<18-->no of years eligibility should tell
negative values -->not acceptable



age=int(input("enter the age:"))
if age>=18 and age<=100:
    print("user has voter eligibility")
    print("----Acess granted----")
elif age<18 and age>0:
    print("user still need to get vote eligibility")
    print("user need to wait for more ",(18-age),"years")
else:
    print("only positive values and less than 100 are acceptable")
'''


'''
#Output formatting
output-->print()-->we can pass any values also use sep and end
% is used here(%d,%f...),format() usage,fstring notation
'''
'''
a,b=7,9
print(a)
print(b)
print(a,b)
name="codegnan";batch="dataanalysis"
print(name,batch)
print(name,batch,sep=',')
print(name,batch,sep='&')
#end='\n,\t-->tabspace
print(a,b,end='')
print("hyderabad")
'''


#Usage of commas
name="codegnan";place="hyderabad";age=7;batch="da-23"
print(batch,'is in',name)
print(name,'is in',place,'age is',age,'years')



'''

#Old style formatting -->%d -->integer, %s-->String, %f-->float
salary = 24253.256
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
print("His Salary is %.1f"%(salary)) #%.1f-->rounding to 1 decimal

#.format() usage
print("{} is in {}".format(name,place)) # oder matters

# fstring usage (more recommended)
print(f'{name} is in {place}')
print(f'{"Vaishnavi"} is in {name}')
'''


