# class method and static method

class Person:
    def  __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    @classmethod

    def object_by_year(cls,name,year):
        return cls(name,2019-year)

    @staticmethod

    def is_adult(age):
        if age>=18:
            return True
        else:
            return False

p1 = Person("lala",4)
p2 = Person.object_by_year("sonu",2000)

print(p1.get_name(),p1.get_age(),Person.is_adult(p1.age))
print(p2.get_name(),p2.get_age(),Person.is_adult(p2.age))
