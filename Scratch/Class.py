class Employee:
    id = 11
    name = "Aparna"
    def display(self):
        print("ID  ",self.id)
        print(" name : ",self.name)
# create object
emp = Employee()
emp1 = Employee()

emp.display()
#delete property of object
del emp.id

#delete object itself
del emp
print(id(emp))
print(id(emp1))