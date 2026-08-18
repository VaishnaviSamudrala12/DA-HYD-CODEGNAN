'''
Mapping-->Dictionary-->collection of key value pairs used to store related data(Ex:JSON,APIs,database records)
dict()-->data={}-->data={key:value}
Dictionary is mutable ,indexed through keys,ordered,heterogenenous
Keys must be uniques(int,strings,float,values...)
'''

details={}
print(type(details))

details={'Id':'CGH3976',
         'Name':'Vaishnavi',
         'Gender':'Female',
         'Age':21,
         'Batch':'DA23',
         'Place':'Hyd'}
print(details)
print(len(details))
'''

#Acess the data from dictionary
#details[0]#this key is not there in dictionary(key error)
print(details.keys())#it returns keys from dictionary
print(details['Id'],details['Name'])
#print(details['marks'])#key error as marks is not present
details['marks']=[]
print(details)
print(type(details['marks']))
details['marks'].append(20)
print(details)
details['marks'].extend([30,37,45,50])
print(details)


#Create a key value pair of practice session
details['PS']=('Mon','Thrus','Sat')
print(details.keys())#keys() returns keys from the dictionaray
print(details['marks'][2])#accessing 3rd day marks of student
print(details['PS'][1])#accessing 2nd day of practice session


details['MI']=('Monday','Wednesday','Friday')
#operations-->mutable,indexing,through keys,membership
print('Wednesday' in details)#returns false
print('MI' in details)#returns true as we have MI as key
for i in details:
    print(i)

for i in details.keys():
    print(f'Key={i}')
    print(details[i])
    print(f'Value={details[i]}')


for i in details.values():#returns value from dictionary
    print(i)

for i in details .items():#returns a key value pair in tuple
    print(i)

for key,value in details.items():
    print(f'key is {key}')
    print(f'Value is {value}')


#update()-->updating the dictionary with key-value pairs
details.update({'marks':[],
                'PS':('Tuesday','Thrusday','Saturday')})
print(details)
details['marks'].extend([25,30,25])
print(details)
marks=list(map(int,input("enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)


print(details.keys())
print(details.get('Name'))
print(details.get('Branch'))#returns none as we dont have branch as the key
print(details.keys())

details.setdefault('Branch')#if key is not present it inserts into dict
print(details)
details['Branch']='CSE'
print(details)
print(details.setdefault('Name'))

#pop
details.pop('Branch')#branch is removed permanently (for pop in dict we need to mention key)
print(details)
print(details.keys())


print(details.popitem())#popitem() will remove and returns a key- value pair as a 2-tuple from last 
print(details.popitem())


del details['Id']
print(details.keys())

details.clear()#removes all elements from dictionary
print(details)


#fromkeys()
data=['saketh','sai','data']
b=dict.fromkeys(data)#creates a dictionary but value set to None
print(b)
b['saketh']=31
print(b)
c=dict.fromkeys(['CGH1234','CGH2345'],['code','gnan'])
print(c)
'''

#Task:create a dictionary with your personal details ,similar to your codegnan profile
details={'Student Name':'Samudrala Vaishnavi','Student Id':'CGH3976',
         'Batch No':'DA-HYD-023','EmailId':'vaishnavisamudrala62@gmail.com',
         'Date of birth':'2005-04-12','Age':'21','Gender':'Female','Blood Group':'O+',
         'City':'Hyderabad','State':'Telangana','Phone No':'xxxxxxxxxx',
         'Github Link':'https://github.com/22r01a6653'}
print(details)



