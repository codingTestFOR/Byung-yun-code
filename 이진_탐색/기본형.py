def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        print(f"DEBUG: start={start}, end={end}, mid={mid}, mid_value={array[mid]}")
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

if __name__ == "__main__":
        print(binary_search([1, 3, 5, 7 ,9, 11, 13, 100, 200, 300, 1000],
                      9,
                      0,
                      10))

