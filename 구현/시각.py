# n = 5
n = int(input())

hours = 0
seconds = 0
minute = 0
count_three = 0  # 3을 셀 변수

while hours <= n:
    if "3" in str(minute) + str(seconds) + str(hours):  # 초, 분, 시 중 3이 포함된 경우
        count_three += 1
    seconds += 1
    if seconds > 59:
        minute += 1
        seconds = 0
    if minute > 59:
        hours += 1
        minute = 0
        seconds = 0

print(count_three)

