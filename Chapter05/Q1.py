# 클래스 다음과 같다.

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

cal=UpgrageCalculator()
# print(cal.add(5))
# print(cal.add(7))
# print(cal.minus(8))
print(cal.add(10))
print(cal.minus((7)))
print(cal.value)