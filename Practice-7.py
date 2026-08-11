'''
#display a sentence in several different letter cases
a=input("enter the string:")
b=a.upper()
print(b)
c=a.lower()
print(c)
d=a.title()
print(d)
e=a.capitalize()
print(e)
f=a.swapcase()
print(f)
print('PYTHON IS FUN'.isupper())
print('python is fun'.islower())
print('python is fun'.istitle())


b=input('enter the string:')
if b.isupper():
    print('it is upper')
elif b.islower():
    print('it is lower')
elif b.istitle():
    print('it is title')
else:
    print('null')
'''




'''
#repeately ask the user for a username and report which validation rules it passes,stop when the user enters quit


a=input("enter the string:")
while a!="quit":
    if a.isalnum():
        print("the username contains only letters and numbers")
    if a.isidentifier():
        print("valid python identifier")
    if a[0].isalpha():
        print("the username begins with character")
    if a.isascii():
        print('it is ascii value')
    else:
        print("null")
    a=input("enter the string:")
'''

'''
->enter the string:100student
the username contains only latters and numbers
it is ascii value

->enter the string:student_name
valid python identifier
the username begins with character
it is ascii value
'''


'''
#formatted student report
students = []
for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks")
        continue

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students.append((name, marks, grade))

print("\n" + "STUDENT REPORT".center(30))
print("=" * 30)
print(f"{'Name'.ljust(15)}{'Marks'.rjust(5)}{'Grade'.rjust(8)}")

for name, marks, grade in students:
    print(f"{name.ljust(15)}{str(marks).rjust(5)}{grade.rjust(8)}")
'''



#Character nd text analyzer
text=input("enter string:")
digit_count=0
letter_count=0
space_count=0
printable_count=0
for i in text:
   if i.isalpha():
       letter_count+=1
   if i.isdigit():
       digit_count+=1
   if i.isspace():
       space_count+=1
   if i.isprintable():
       printable_count+=1
print("Letters :",letter_count)
print("Digits :",digit_count)
print("Spaces :",space_count)
print("Printable :",printable_count)
print("Title case: ",text.istitle())
print("Upper case: ",text.isupper())
print("Lower case :",text.islower())
