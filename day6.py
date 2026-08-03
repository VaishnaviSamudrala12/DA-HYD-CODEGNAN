#Repetition Statements(loops)-->for ,while,(for with else),(while with else),loops tells how much time should we use conditional statements
#Jumping Statements-->break,continue,pass
'''
Loops:loops are helpful for repetition (Automation tasks)
for keyword will be helpful to iterate over a sequence/range
Syntax of for keyword:
for <temp_var> in sequence/range:
    statement(s)...
'''

'''
#range(start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
#in above case we got 10 iterations
#range(stop)-->default 0 ends at stop-1
for i in range (1,10):
    if i>5:
        print(f'value of i is -->{i}')
for i in range(1,10):
    if i>5 and i%2==0:
        print(f'final value of i is-->{i}')
'''

'''
#range(step)-->interval
for i in range (1,10,2):
    print(i)
    print("done")
'''
'''
#it returns counter in reverse order
for i in range (-10,0,-1):
    print(i)
for i in range (-10,0,1):
    print(i)
'''

'''
#[]--> lists in for
names=['vaishnavi','jashnavi','vidya']
for name in names:
    print(names)
    print(f'student name is {name}')
'''


'''
names=['vaishnavi','jashnavi','vidya']
print(len(names))#len(obj)-->returns the no of items in a container
for name in names:
    print(names)
    print(f'student name is {name}')
'''

'''
names=['vaishnavi','jashnavi','vidya']
for name in names:
    if name =="vaishnavi":
        print(f'student name is {name}')
'''



'''
#calculate the sum of first 10 numbers
first understand the input-->range(11)
second understand your output-->sum(number)
third we need to map the logic
'''
'''
result=0 #target variable
for i in range (11):
    result=result+i #result +=i
    print(f'now the result is {result}')
    print(f'sum of 10 numbers is {result}')
'''

'''
#sum of first 10 even numbers
result=0
for i in range(1,21):
    if i%2==0:
        result +=i
        print(f'now the result is {result}')
'''


#Understand the loops usage with fitness streak example(workout-->1,workout_missed-->0)
work_log=[0,1,1,1,0,1,0]
longest_streak=0
current_streak=0
for day in work_log:
    #print(day)
    if day==1:
        #print(day)
        current_streak= current_streak + 1
        if current_streak > longest_streak:
            longest_streak=current_streak
        
    else:
        current_streak=0
print(f'longest_streak is {longest_streak}')
            
