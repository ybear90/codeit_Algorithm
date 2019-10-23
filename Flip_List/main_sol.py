"""
리스트 some_list의 길이를 n이라고 합시다.

일단 재귀 부분을 제외한 부분부터 평가해 봅시다.

우선 base case 부분은 그냥 O(1)입니다. Recursive case 부분은 재귀적 호출을 제외하면 some_list[-1:]과 some_list[:-1]에 대한 평가를 해야 하는데요.

some_list[-1:]은 시간 복잡도가 O(1)이고, some_list[:-1]은 시간 복잡도가 O(n−1)입니다. 재귀적 부분을 제외한 flip 함수의 시간 복잡도는 O(n)인 거죠.

그렇다면 flip 함수는 몇 번 호출될까요? 매 호출마다 리스트의 길이가 1씩 줄기 때문에, flip 함수는 총 n번 실행됩니다.

flip 함수는 재귀적으로 n번 실행되고 각 호출은 O(n)이기 때문에 총 시간 복잡도는 O(n2)입니다.
"""

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # base case
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list

    # recursive case
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)