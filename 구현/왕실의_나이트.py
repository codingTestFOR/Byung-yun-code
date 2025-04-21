user_input = input()

col = ord(user_input[0]) - ord('`')  # 아스키 코드에서, ` = 96, a = 97
row = int(user_input[1])

move_patterns = ((2, 1), (1, 2), (-2, 1), (-1, 2),      # 나이트가 이동하는 패턴의 수는
                 (2, -1), (1, -2), (-2, -1), (-1, -2))  # 여덟 가지다.

count = 0
for move in move_patterns:
    delta_row = move[0]
    delta_col = move[1]

    if col + delta_col < 1 or col + delta_col > 8: continue  # 맵 나가면
    if row + delta_row < 1 or row + delta_row > 8: continue  # 카운트 안 함
    # print(col + move[0], " ", row + move[1])
    count += 1

print(count)
