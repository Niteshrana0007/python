# create a base class of person
class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname +" "+self.lastname
# create employee class by inheriting Person class

class Employee(Person):
    def __init__(self,first,last,staffnum):
        super().__init__(first,last)
        self.staffnumber = staffnum

    def getEmployee(self):
        return self.name()  +" "+ str(self.staffnumber)

# using Employee class

x = Person("Ram","Prasad")
y = Employee("Om","Shri",2341)

print(x.name())
print(y.getEmployee())
