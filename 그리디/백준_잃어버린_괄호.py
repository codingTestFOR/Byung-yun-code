"""
55-(50+40), -35

10+20+30+40, 100

00000-00000, 0

10+10+10+10-10, 30

처음에 음수는 나오지 않음
풀이 아이디어: 처음 나온 '-' 이후 모든 값을 더하고 처음 양수에서 뺀다.
"""

data = input()
# data = "55-50+40-50+50"
# data = "10+20+30+40"
# data = "55-50+40-50+50"

result = 0

split_data = data.split("-")
is_only_plus = True if len(split_data) <= 1 else False
# print(split_data)
if is_only_plus:  # 마이너스 없는 경우
    numbers = list(map(int, split_data[0].split("+")))
    result = sum(numbers)
else:  # 마이너스가 하나라도 존재하는 경우
    idx = data.find("-")

    first = data[:idx].split('+')
    second = data[idx+1:].replace('+', '-').split('-')
    #print(first)
    # print(second)
    result = sum(list(map(int, first))) \
             - sum(list(map(int, second)))

print(result)
