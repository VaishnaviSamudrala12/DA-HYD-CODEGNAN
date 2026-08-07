'''
#to print given list in serial no wise
movies=input("enter the name of movie").split()
i=1
for movie in movies:
    print(i,movie)
    i+=1
'''
'''
#fibanocci series
m=int(input("enter the values"))
a=0
b=1
for i in range(m):
      print(a,end=" ")
      c=a+b
      a=b
      b=c
    
'''
'''
#using while loop
num=int(input("enter values:"))
a=0
b=1
i=0
while i<num:
    print (a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1
'''

'''
#write a python program to calculate the innings of a batsman and count the boundaries,dot balls,total score
#list=[4,6,1,0,2,4,0,6]
runs=list(map(int,input("enter no.of runs:").split(',')))
boundaries=dotballs=total_score=0
for i in runs:
    total_score+=i
    if i==4 or i==6:
        boundaries+=1
    elif i==0:
        dotballs+=1
print('boundaries:',boundaries)
print('dotballs:',dotballs)
print('total_score:',total_score)
'''
'''
#phone password attempts
password='3637'
max_attempts=5
current_attempt=0
while current_attempt<max_attempts:
    entered_password=input("enter password:")
    if entered_password==password:
        print("Unlocked")
        break
    else:
        print("entered password is wrong.Try again")
        current_attempt+=1
else:
    print("phone locked try after 30 seconds")
'''


#ATM pin verification
pin="2005"
max_attempts=3
current_attempt=0
while current_attempt<max_attempts:
    entered_pin=input("enter pin:")
    if entered_pin==pin:
        print("login successful")
        break
    else:
        print("entered pin is wrong.try agin")
        current_attempt+=1
else:
    print("limit reached.try after 24 hours")
        

    
