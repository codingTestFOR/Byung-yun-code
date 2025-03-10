total = 7
repeat = 2
number_list = [3, 4, 3, 4, 3]

result = 0
count = 0
number_list.sort(reverse=True)
print(number_list)

for i in range(0, total):
    if count < repeat:
        result += number_list[0]
        count += 1
    else:
        result += number_list[1]
        count = 0

print(result)
