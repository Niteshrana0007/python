# calculator using class
class cal:
    def __init__(self,num1,num2):
        self.number1 = num1
        self.number2 = num2

    def add(self):
        return self.number1+self.number2

    def sub(self):
        return self.number1-self.number2

    def div(self):
        return self.number1/self.number2

    def pro(self):
        return self.number1*self.number2


obj = cal(2,2)
print(obj.add())
print(obj.sub())
print(obj.div())
print(obj.pro())
