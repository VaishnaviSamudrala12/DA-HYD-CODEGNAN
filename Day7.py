'''
Usage of else with for-->the else keyword will only be executed when the loop is completely
done without any break
'''
'''
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
            print(longest_streak)
        
    else:
        current_streak=0#streak breaks
else:
    print(f'longest_streak is {longest_streak}')
'''



'''
#break usage
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
            print(longest_streak)
            break
        
    else:
        current_streak=0#streak breaks
else:
    print(f'longest_streak is {longest_streak}')
print("execution done")
#In this case when the entire loop execution is done we get result of else block
'''


'''
#for-else with notifications scenario
notifications=[0,0,0,0]
for notification in notifications:
    if notification==1:
        print("unread notification")
        
else:
    print("all caught up")



#
notifications=[0,0,1,0]
for notification in notifications:
    if notification==1:
        print("unread notification")
        break
else:
    print("all caught up")



#try to take notifications from user -->list of integers
notifications=list(map(int,input("enter the values-->0 or 1:").split(',')))
for notification in notifications:
    if notification==1:
        print("unread notification")
        break
else:
    print("all caught up")
'''



'''
#while--> it relies on ondition,it will be completely executed until the condition is satisfied
Syntax:
while <condition>:
    statement(s)...


while(True):#it prints infinite times yes so we use cntrl+c to stop the loop(keyboard interrupt)
    print("yes")
'''

'''
i=0#intialised statement
while i<=10:
    print(i)
    i=i+1#counter object or counter

i=10
while i>=1:
    print(i)
    i=i-1#i-=1


i=0
while i<=10:
    print(10-i)
    i=i+1
'''


#banking scenario-->PIN authentication if more than 3 attempts account locked
pin="2612"
max_attempts=3
current_attempt=0
while current_attempt<max_attempts:
    entered_pin=input("enter the ATM pin:")
    if entered_pin==pin:
        print("Login Sucessful")
        break#stops loop execution
        #continue-->it holds forthiscondition and skips to the next part of the code
    else:
        print("Entered PIN is wrong.. Try again carefully")
        current_attempt+=1
else:
    print("Account locked try after 24 hrs")
