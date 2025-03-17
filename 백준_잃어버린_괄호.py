"""
55-(50+40), -35

10+20+30+40, 100

00000-00000, 0

10+10+10+10-10

가장 처음과 마지막은 숫자, 처음 마이너스값이 나오는 경우는 없음
최소화 시키기 위해선 (-)를 다음 (-)가 나오기 전까지 괄호로 묶는다.
1. ●+●+●+●+●...
2. ●-(●+●)-(●+●)
4. ●+●-(●+●)-●
3. ●-●-●-●-
"""

data = input()
# data = "55-50+40-50+50"
# data = "10+20+30+40"
# data = "55-50+40-50+50"

result = 0

split_data = data.split("-")
is_only_plus = True if len(split_data) <= 1 else False
# print(split_data)
if is_only_plus:  # 마이너스 없음
    numbers = list(map(int, split_data[0].split("+")))
    result = sum(numbers)
else:  # 마이너스가 하나라도 존재함
    idx = data.find("-")

    first = data[:idx].split('+')
    second = data[idx+1:].replace('+', '-').split('-')
    #print(first)
    # print(second)
    result = sum(list(map(int, first))) \
             - sum(list(map(int, second)))

print(result)