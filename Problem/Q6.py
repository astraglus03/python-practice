# 총합구하기

numbers = input("숫자를 입력하세요 (쉼표로 구분): ")
number_list = numbers.split(",")  # 입력된 문자열을 쉼표로 구분하여 리스트로 저장
total = 0
for num in number_list:
    total += int(num)  # 리스트에 있는 각 숫자를 정수로 변환하여 총합 계산
print("입력한 숫자의 총합은", total, "입니다.")