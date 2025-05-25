# 디버그
n = 5
store_parts = [8, 3, 7, 9, 2]
m = 3
order_parts = [5, 7, 9]

# 입력
# n = input()
# store_parts = list(map(int, input().split()))
# m = input()
# order_parts = list(map(int, input().split()))

# 이진 탐색을 위한 정렬
store_parts.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return print("yes", end=' ')
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return print("no", end=' ')


for p in order_parts:
    binary_search(store_parts, p, 0, n - 1)