"""
문제 번호: 1339

예제 입력
n = 2
strings = ['GCF", "ACDEB"]
"""

# 입력
n = int(input())  # 2
strings = []
for i in range(n):  # GCF, ACDEB
    strings.append(input())

# 1. 가중치 설정
weights = {}  # 알파뱃과 가중치를 넣을 딕셔너리
for string in strings:
    char_list = list(string)  # reverse 함수를 사용하기 위해서
    char_list.reverse()  # FCG, BEDCA
    weight = 1

    for char in char_list:
        if char in weights:
            weights[char] = weights[char] + weight
        else:
            weights[char] = weight
        weight = weight * 10


# weights = {'F': 1, 'C': 1010, 'G': 100, 'B': 1, 'E': 10, 'D': 100, 'A': 10000}

# 2. 숫자 할당
weights = dict(sorted(weights.items(), key=lambda x:x[1], reverse=True))
count = 9
for i in weights.keys():
    weights[i] = count
    count = count -1

# weights = {'A': 9, 'C': 8, 'G': 7, 'D': 6, 'E': 5, 'F': 4, 'B': 3}

# 3. 문자를 숫자로
numbers = []  # 최종 숫자들를 담을 리스트
for string in strings:
    for char in string:
        string = string.replace(char, str(weights[char]))
    numbers.append(int(string))

# numbers = [784, 98653]

# 4. 합계 계산
sum = 0
for n in numbers:
    sum = sum + n

print(sum)
