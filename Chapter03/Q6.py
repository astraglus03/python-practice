#리스트 중에서 홀수에만 2를 곱하는 코드는 다음과같다

numbers=[1,2,3,4,5]
result=[]
for n in numbers:
    if n%2==1: result.append(n*2)
print(result)
# 위 코드를 리스트 내포를 사용하여 표현해보자
numbers=[1,2,3,4,5]
result=[]
result=[i*2 for i in numbers if i%2==1]
print(result)