#  A  \  B  0  1  2  3  4
#  0
#  1
#  2
#  3
#  4
#

n, m = 4, 4
a, b = 1, 1
direction = 0  # 0: 북, 1: 동, 2: 남, 3: 서
area = [
    (1, 1, 1, 1),
    (1, 0, 0, 1),
    (1, 1, 0 ,1),
    (1, 1, 1 ,1)
]

visited_area = [[0] * m for _ in range(n)]
visited_area[a][b] = 1  # 시작 위치 1

da = [-1, 0, 1, 0]
db = [0, 1, 0 ,-1]

direction_dict = {0: '북', 1: '동', 2: '남', 3: '서'}

count = 1  # 총 방문한 타일 수
turn_count = 0

def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

while True:
    print(f'a: {a}, b: {b}, d: {direction_dict[direction]}')
    turn_left()
    new_a = a + da[direction]
    new_b = b + db[direction]
    if area[new_a][new_b] == 0 and visited_area[new_a][new_b] == 0:  # 땅이 맞는가 확인
        visited_area [new_a][new_b] = 1  # 방문했다는 걸 기록
        # 실제로 이동
        a = new_a
        b = new_b
        count += 1  # 총 밟은 타일 추가
        turn_count = 0  # 돈거 초기화
        continue
    else:  # 어라 한 번 더 돌아야지
        turn_count += 1
    if turn_count >= 4:  # 뒤로 한 칸
        new_a = a - da[direction]
        new_b = b - db[direction]
        if area[new_a][new_b] == 0:  # 땅인가?
            a = new_a
            b = new_b
        else:  # 으악 바다에 빠짐
            break
        turn_count = 0

print(count)