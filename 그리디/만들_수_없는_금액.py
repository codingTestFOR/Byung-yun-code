# 1 1 1 3 8
# count를 하나씩 높이면서 비교하기
data = input('data : ')
data = list(map(int, data.split()))

data.sort()
target = 1  # 이거 만들 수 있냐?
for x in data:
    print(x, target)
    if x > target:  # 못해
        break
    target += x

print(target)

"""
target - 1: 만들 수 있는 최댓값
target이 3까지 갔다고 하자.
여기서 x가 3이라면
최대 6까지 만들 수 있어서 target이 6까지 늘어나는 거임
왜냐하면 3까지 만들 수 있으니까 1과 2도 만들 수 있곘지 
target -1까지는 어떻게든 만들 수 있다.
5원까지는 확정이라는 거임
"""
