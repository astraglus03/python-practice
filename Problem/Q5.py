# 피보나치 수열 더하기
def plus(n):
    if(n==0): return 0
    if(n==1): return 1
    return plus(n-2)+plus(n-1)

for i in range(10):
    print(plus(i), end=" ")