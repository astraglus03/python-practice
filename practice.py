from copy import copy

print("hello")
print("hi")

a=[1,2,3]
# b=copy(a)
b=a[:]
print(b)

a=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in a:
    if(i%3!=0):sum=sum+i;
print(sum)

marks=[90,25,67,45,80]
number=0
for i in marks:
    number+=1
    if(i<60): print("%d번째 학생 넌 낙제다" %number)
    else:continue


a=range(1,101)
sum=0
for i in a:
    sum+=i
print(sum)

for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j, end=" ") # end사용시 다음줄로 넘기지않고 그줄에서 계속 실행시키기 위함
    print("")

a=[1,2,3,4]
result=[i*3 for i in a] # 유용할듯..
print(result)

result=[i*j for i in range(1,10)
        for j in range(2,10) ]
print(result)
# 어떤건 print할수 있고 할수 없는것들이 있음
def add(a,b):
    print("%d,%d의 합은 %d입니다" %(a,b,a+b))

print(add(3,4))


def say(nick):
    if nick  =="바보": return("나의 별명은 %s입니다" %nick)

say("바보")