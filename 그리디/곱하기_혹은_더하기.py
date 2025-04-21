# 곱하기 혹은 더하기

data_1 = "110122"

def calculate(data):
    numbers = [int(n) for n in data]  # [0, 2, 9, 8, 4]

    result = numbers[0]

    for number in range(1, len(numbers)):  # range(1, len(numbers)) == [2, 9, 8, 4]
        if numbers[number] <= 1 or result <= 1:
            result += numbers[number]
        else:
            result *= numbers[number]

    return result

answer_1 = calculate(data_1)
print("출력 예시 1 : %d" % answer_1)  # 576

