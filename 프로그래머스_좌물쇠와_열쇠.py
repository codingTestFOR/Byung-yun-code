
def invert_matrix(array):
    return [[1 - cell for cell in row] for row in array]

def rotate_90d(array):
    n = len(array)  # 행 길이
    m = len(array[0])  # 열 길이
    result = [[0] * n for _ in range(m)]  # 새로운 같은 크기의 배열

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = array[i][j]
            # 90도 회전한 후 행 번호 = 회전하기 전 열 번호
            # 90도 회전한 후 열 번호 = N - 1 - 회전하기 전 행 번호
            # (열, 행)
            # 3, 0 => 3, 3
    return result


def solution(key, lock):

    # 비교하기 쉬운 자물쇠 만들기
    final_lock = invert_matrix(lock)

    x_offset_min  = - len(key) + 1
    x_offset_max = len(lock) - 1

    y_offset_min = x_offset_min
    y_offset_max = x_offset_max

    x_offset = x_offset_min
    y_offset = y_offset_min
    turn_count = 0


    while y_offset <= y_offset_max:  # 맵을 나가면 실패
        key_2 = list(key)
        final_key = []  # 실재 열쇠 값을 바꾸는 대신 가상의 열쇠 생성

        # 열쇠 끼우는 실제 부분 구하기

        # 열쇠 회전
        if turn_count > 0:
            for i in range(turn_count):
                key_2 = rotate_90d(key_2)

        # x축 이동
        if x_offset > 0:
            for i in key_2:
                new_row = list(i)
                for j in range(abs(x_offset)):
                    new_row.insert(0, 0)
                    new_row.pop()
                final_key.append(new_row)
        elif x_offset < 0:
            for i in key_2:
                new_row = list(i)
                for j in range(abs(x_offset)):
                    new_row.append(0)
                    new_row.pop(0)
                final_key.append(new_row)
        else:
            final_key = list(key_2)

        # y축 이동
        if y_offset > 0:
            for i in range(y_offset):
                final_key.append([0] * len(key))
                final_key.pop(0)
        elif y_offset < 0:
            for i in range(abs(y_offset)):
                final_key.insert(0, [0] * len(key))
                final_key.pop()

        print('x: ', x_offset, '. y:', y_offset, '. turn: ', turn_count)
        print('final:', final_key)

        # 맞는지 확인
        if final_key == final_lock:
            return True

        # 후처리
        if turn_count < 3:  # 열쇠 돌리기
            turn_count += 1
        else:  # 열쇠 옮기기
            turn_count = 0
            x_offset += 1
            if x_offset > x_offset_max:
                y_offset += 1
                x_offset = x_offset_min

    answer = False
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

"""
KEY
□ □ □
■ □ □
□ ■ ■

LOCK
■ ■ ■
■ ■ □
■ □ ■

x_offset = 1일 경우

□ □ □
□ ■ □
□ □ ■

y_offset = 1일 경우
■ □ □
□ ■ ■
□ □ □

y_offset = -1일 경우

□ □ □
□ □ □
■ □ □
"""