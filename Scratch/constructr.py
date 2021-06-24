class Employee:
    #perameterised constructor
    def __init__(self,name,id):
        self.id = id
        self.name = name

     


    def display(self):
        print("ID :  ",self.id)
        print("Name : ",self.name)
# create object
emp = Employee("Johne",101)

emp1 = Employee("David",102)

#accessing display() method to print employee  information
emp.display()
#accessing display() Method  to print employee 1 information
emp1.display()
