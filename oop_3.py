# using inheritance in calculator
from oop_2 import cal

class average(cal):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)

    def avg(self):
        return self.add()/2



ob1 = average(2,2)
print(ob1.avg())
