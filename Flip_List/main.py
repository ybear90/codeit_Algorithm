# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    new_list = []
    # 여기 실수
    if len(some_list) == 1 or len(some_list) == 0:
        new_list.append(some_list.pop())
        return new_list

    # Recursive Case
    tail = some_list.pop()
    new_list.append(tail)

    return new_list + flip(some_list)

    # Recurvise Case(another sol)
    # return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)