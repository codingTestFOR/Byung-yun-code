S = input()
alpha = []
count = 0
for i in S:
    if ord("A") <= ord(i) <= ord("Z"):
       alpha.append(i)
    else:
        count += int(i)

alpha.sort()
if count == 0:
    print("".join(alpha))
else:
    print("".join(alpha) + str(count))