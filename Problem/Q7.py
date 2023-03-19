# 입력받은 구구단 출력하기

a=int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
for i in range(1,10):
    print(a*i,end=" ")
