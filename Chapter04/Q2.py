# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자(입력으로 들어오는 개수 미정)

def avg_numbers(*args):
    result = 0
    for i in args:
        result = result + i
    return result/len(args) # 들여쓰기 잘하자


print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))
