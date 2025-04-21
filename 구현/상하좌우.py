# n = int(input())
# route = input().split()

n = 5
route = "R R R U D D"
route = route.split()

x, y = 1, 1
for r in route:
    if r == "U":
        if y <= 1:
            continue
        else:
            y -= 1
    elif r == "D":
        if y >= n:
            continue
        else:
            y += 1
    elif r == "L":
        if x <= 1:
            continue
        else:
            x -= 1
    elif r == "R":
        if x >= n:
            continue
        else:
            x += 1
    print("%d, %d" % (y, x))

# print("%d, %d" % (x, y))

