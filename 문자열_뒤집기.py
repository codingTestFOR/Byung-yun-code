"""
0011001100
11001100
0001100
"""

data = input('data : ')
data = list(map(int, data))

count_zero = 0
count_one = 0
mode = 2

for i in data:  # 0과 1을 번갈아가면서 세보기
    if i == 0:
        if mode == 0:
            continue
        else:
            mode = 0
            count_zero += 1
    else:
        if mode == 1:
            continue
        else:
            mode = 1
            count_one += 1

result = count_zero if count_zero <= count_one else count_one


print(result)