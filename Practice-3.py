'''
#Sum of items in a cart 
result=0
product=list(map(int,input("enter amount of each product:").split(',')))
for products in product:
    result += products
print(result)
'''

'''
#Password analyzing
password=input("enter password:")
upper=lower=digit=special=0
for ch in password:
    if 'A'<=ch<='Z':
        upper+=1
    elif 'a'<=ch<='z':
        lower+=1
    elif '0'<=ch<='9':
        digit+=1
    else:
        special+=1
print("upper:",upper)
print("lower:",lower)
print("digit:",digit)
print("special:",special)
'''


'''
#return domain of the email entered
email=(input("enter email:").split(','))
for mail in email:
    print(mail.split("@")[1])
'''
'''
#return ott history in orderwise
movieorder=0
movielist=list(map(int,input("enter movies")))
for movies in movielist:
    if movies>1:
 '''       

