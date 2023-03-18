# A학급에 총 10명의 학생이 있다. for문 사용하여 A학급 평균 구하시오

A=[70,60,55,75,95,90,80,80,85,100]
total=0
for i in A:
    total+=i

average=total/len(A)
print(average)