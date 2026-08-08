'''
#find secret number
secret="123"
while True:
    entry=input("enter key:")
    if secret==entry:
        print("key is correct")
        break
    print("try again..")
'''

'''
#otp verification
otp="3637"
cur_attempt=0
max_attempt=7
while cur_attempt<max_attempt:
    entry=input("enter otp:")
    if otp==entry:
        print("otp is correct")
        break
    else:
        print("re-enter")
        cur_attempt+=1
else:
    print("limit reached")
'''

'''
#Taking food orders
food=input("enter items:")
count=0
while food!="exit":
    count+=1
    food=input("enter items:")
print("total no of items ordered:",count)
'''

#game with 3 chances
word="python"
chances=3
attempt=1
while attempt<=3:
    entry= input("enter word:")
    if word==entry:
        print(f'You won! you have {chances-attempt} chances')
        break
    else:
        print(f'You lost.. you have {chances-attempt} chances')
        attempt+=1
