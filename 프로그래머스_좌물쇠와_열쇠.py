# 열쇠의 가장 오른쪽 아레 부분부터 돌려가며 자물쇠에 대입하고
# 열쇠의 가장 왼쪽 위 부분까지 맞춰본다.
from typing import final


def solution(key, lock):


    def turn_key():
        return

    x_offset_min  = - len(key) + 1
    x_offset_max = len(lock) - 1

    y_offset_min = x_offset_min
    y_offset_max = x_offset_max

    x_offset = x_offset_min
    y_offset = y_offset_min


    while y_offset <= y_offset_max:
        final_key = []
        final_key2 = []
        # 열쇠 끼우는 실제 부분 구하기
        if x_offset > 0:
            for i in key:
                new_row = list(i)
                for j in range(abs(x_offset)):
                    new_row.insert(0, 0)
                    new_row.pop()
                final_key.append(new_row)
        elif x_offset < 0:
            for i in key:
                new_row = list(i)
                for j in range(abs(x_offset)):
                    new_row.append(0)
                    new_row.pop(0)
                final_key.append(new_row)
        else:
            final_key = list(key)




        print('final:', final_key)

        # 맞는지 확인


        # 열쇠 돌리기

        # 열쇠 옮기기
        x_offset += 1
        if x_offset > x_offset_max:
            y_offset += 1
            x_offset = x_offset_min



    answer = False
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

"""
□ □ □
■ □ □
□ ■ ■


x_offset = 1일 경우

□ □ □
□ ■ □
□ □ ■

y_offset = 1일 경우

□ □ □
□ □ □
■ □ □
"""