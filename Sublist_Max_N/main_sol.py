"""
아래 리스트를 예시로 생각을 해 봅시다.

profits = [7, -3, 4, -8]
profits의 최대 수익은 아래 두 가지 중 하나입니다.

부분 문제 [7, -3, 4]의 최대 수익 (sublist_max([7, -3, 4]))
부분 문제 [7, -3, 4, -8]에서 -8 을 포함한 구간의 최대 수익
첫 번째 경우는 당연하죠? 최대 수익 구간에 마지막 요소가 포함되지 않을 때 최대 수익은 부분 문제와 똑같습니다.

두 번째 경우는 첫 번째와는 반대되는 경우인데요. 마지막 요소 -8가 포함돼서 최대 수익이 기존 값에서 변하는 경우죠.

-8가 포함되는 구간은 -8이 포함된 구간들은 총 네 개의 구간이 있습니다.

[-8]
[4, -8]
[-3, 4, -8]
[7, -3, 4, -8]
이 구간들의 최대 수익이 바로 두 번째 경우죠.

첫 번째 경우는:

max_profit_so_far = sublist_max([7, -3, 4])
두 번째 경우는:

max_check = max(sum([-8]), sum([4, -8]), sum([-3, 4, -8]), sum([7, -3, 4, -8]))
이렇게 표현할 수 있겠네요.

sublist_max(profits)는,

max_profit_so_far = sublist_max([7, -3, 4])
max_check = max(sum([-8]), sum([4, -8]), sum([-3, 4, -8]), sum([7, -3, 4, -8]))
이 두 값 중 더 큰 값이고, 코드로 나타내면,

max_profit_so_far = max(max_profit_so_far, max_check)
이렇게 표현할 수 있습니다. For 문을 돌면서 각 요소까지의 max_profit_so_far과 max_check를 효율적으로 구할 수 있는 방법에 대해서 생각해보세요.

두 정보 다 바로 전 부분 문제에서 받아올 수 있는 정보를 이용해서 효율적으로 알아낼 수 있는데요.

max_profit_so_far = sublist_max([7, -3, 4]) 이 정보는 바로 전 요소까지의 부분 문제의 답을 그대로 쓰면 되겠죠?

max_check도 마찬가지인데요.

max_check_1 = max(sum([-8]), sum([4, -8]), sum([-3, 4, -8]), sum([7, -3, 4, -8]))를 하나하나 계산할 필요 없이,

바로 전 부분 문제에서 계산한 max_check_2 = max(sum([4]), sum([-3, 4]), sum([7, -3, 4]))을 구했을 때의 값 저장해놓았으면,

max_check_1 = max(max_check_2 - 8, -8)
이렇게 구할 수 있겠죠?

이 문제는 인풋 리스트 profits의 길이가 n이라고 했을 때 n에 비례하는 For 문이 하나가 있죠? 그렇기 때문에 총 시간 복잡도는 O(n)이 됩니다.

Brute Force 방법을 사용했을 때와, Divide and Conquer 방법을 사용했을 때 보다 훨씬 더 시간 복잡도가 좋아졌네요!
"""

def sublist_max(profits):
    max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합

    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        max_check = max(max_check + profits[i], profits[i])

        # 최대 구간 합을 비교를 통해 정한다
        max_profit_so_far = max(max_profit_so_far, max_check)

    return max_profit_so_far


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))