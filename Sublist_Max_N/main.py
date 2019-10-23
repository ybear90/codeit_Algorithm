"""
이미 sublist_max 함수를 각각 Brute Force과 Divide and Conquer 방식으로 작성했는데요.

Brute Force로 풀었을 때는 시간 복잡도가 O(n2), Divide and Conquer를 사용했을 때는 O(nlgn)였습니다.

이번 과제에서는 시간 복잡도를 O(n)로 한 번 더 단축해보세요!

과제 설명은 저번 챕터를 참고하세요!
"""
def reverse_max(profits):
    if len(profits) == 1:
        return profits[0]
    else:
        return max(reverse_max(profits[:-1]) + profits[-1], profits[-1])

def sublist_max(profits):
    # 코드를 작성하세요.
    if len(profits) == 1:
        return profits[0]

    max_profit_so_far = sublist_max(profits[:-1])
    max_after = reverse_max(profits)

    print("current max_profit_so_far: ", max_profit_so_far, "current_max_after: ", max_after)

    return max(max_profit_so_far, max_after)


# 테스트
print(sublist_max([7, -3]))
print(sublist_max([7, -3, 4]))
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))