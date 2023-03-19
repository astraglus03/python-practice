# value가 100이상의 값 가질수 없도록 해라

class Calculator:
    def __init__(self):
        self.value=0

    def add(self,val):
        self.value+=val
        return self.value

class UpgrageCalculator(Calculator):
    def minus(self,val):
        self.value-=val
        return self.value
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value+=val
        if self.value>100: self.value=100
        return self.value;


cal=MaxLimitCalculator()
cal.add(50)
cal.add(40)

print(cal.value)