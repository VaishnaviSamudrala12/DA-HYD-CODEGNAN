'''
Sequences-->Strings,Lists,Tuples,Sets,Frozenset
Mapping -->Dictionary
'''


'''
#Sets--> a  set is unique collection of objects,unorders,mutable,hashing,unindexed:set is represented as set(),{}
#a={} it is an empty dictionary
a=set()
print(type(a))
stud_id={123,345,234,564,234}#it is a set as objects are defined inside
print(stud_id)
print(type(stud_id))
print(len(stud_id))#duplicates are not counted
#print(stud_id[2])#gives error as set cannot find index as it is unorderd
print(234 in stud_id)
#print(stud_id*2)#returns error as set is unique,set cant be repeated
#print(stud_id +stud_id)#two sts cannot be merged
'''

'''
#data={12,3,4,5,[12,3,4],'saketh'}
#print(data0#no lists inside a set as lists are mutable
data={12,3,4,5,(12,3,4),'saketh'}#tuples are immutable
print(data)
print(len (data))
for i in data:
    print(i)#loop can be used to access each object,object position cannot be known in sets as unordered
'''


'''
#Methods on sets -->add(),update(),remove(),discard(),pop()
names={'vaishnavi','jashnavi','vidya','harshitha'}
print(names)
print(len(names))

#ADD
names.add('geetha')
print(names)
names.add('vaishnavi')
print(names)
print(len (names))
#names.add('Vaishnavi','Geetha')#throws error as set can add only one object once
#print(names)
names.add(('varshika','pavani'))#possible because tuple is passed here
print(names)

#UPDATE-->we can update multiple elements in set
da_names={'chotu','geetha','sai','sonu'}
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))
'''


'''
#REMOVE-->remove(),discard(),pop(),clear()

#remove()--> removes an element from the set (it must be a member)
da_names.remove('sai')
print(da_names)
#da_names.remove('sai')#raises key error as sai is already removed
#print(da_names)

#discard()-->will remove an element if it is present else it ignores it but doesn't raise error
da_names.discard('codegnan')#ignores as this object is not present in the set
print(da_names)


#pop()
da_names.pop()#removes and returns an arbitary element
print(da_names)
da_names.pop()
print(da_names)

#clear()-->clears the entire set and returns an empty set as set()
da_names.clear()
print(da_names)

da_names.add('joveriya')
print(da_names)
da_names.update(['sai','akash'])
print(da_names)


#copy()-->creates a shallow copy of set(indepent of each other)
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)#prints  the set along with updated objects
print(da_names)#returns the old set only
'''


'''
#Mathematical Operationson sets-->union(),intersection(),difference(),symmetric difference(),issubset(),issuperset(),isdisjoint()
union-->(|)or(.union),intersection-->(&) or (.intersection)
'''

da_23={12,13,34,56}
da_24={38,12,13,23}

'''
#union(|)
#print(da_23.union(da_24))
event=da_23.union(da_24)#can be performed with any no of sets
print(event)
print(len(event))

#intersection(&)
common=da_23.intersection(da_24)#can be performed with only 2 sets
print(common)
print(len(common))

common=da_23 .intersection_update(da_24)
print(common)
print(da_23)


#difference(-)-->removes common elements and prints remaining elements only from the first list
print(da_23)
print(da_24)
diff=da_23.difference(da_24)
print(diff)
f=da_23-da_24
print(f)


#symmetric difference(^)-->removes common elements and prints all remaining together
symm=da_23.symmetric_difference(da_24)
print(symm)
h=da_23^da_24
print(h)


#issubset()-->returns true if all the elements in set2 are present in set1
#issupersrt()-->returns true if set1 has all elements present in set2
da_24.remove(12)
da_23.remove(13)
print(da_24.issubset(da_23))
print(da_24.issuperset(da_23))


#isdisjoint()returns false for sets having common elements and true if no common elements
print(da_23.isdisjoint(da_24))
'''

#Length of Unique student ids in a class,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids

n = int(input())
student_ids = input().split()
#print(student_ids)
result = set(student_ids)
print(len(result))
    
