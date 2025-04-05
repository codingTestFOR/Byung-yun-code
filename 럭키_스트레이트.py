N = input()
middle = int(len(N) / 2)
first = N[:middle]
second = N[middle:]
first_sum = sum(list(map(int, first)))
second_sum = sum(list(map(int, second)))
if first_sum == second_sum:
    print("LUCKY")
else:
    print("READY")
