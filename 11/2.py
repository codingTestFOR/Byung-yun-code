# 곱하기 혹은 더하기

data_1 = "02984"
data_2 = "567"

def calculate(data):
    numbers = [int(n) for n in data]

    result = numbers[0]

    for number in range(1, len(numbers)):  # range(1, len(numbers)) == [2, 9, 8, 4]
        if number == 0 or result == 0:
            result += numbers[number]
        else:
            result *= numbers[number]

    return result

answer_1 = calculate(data_1)
print("출력 예시 1 : %d" % answer_1)  # 576

answer_2 = calculate(data_2)
print("출력 예시 1 : %d" % answer_2)  # 210
