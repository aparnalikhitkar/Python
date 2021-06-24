#Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s= Student("abc",400)

print(getattr(s,'name'))
print(getattr(s,'marks'))

print("After Modify")

setattr(s,"name","xyz")
setattr(s,"marks",430)

print(getattr(s,'name'))
print(getattr(s,'marks'))