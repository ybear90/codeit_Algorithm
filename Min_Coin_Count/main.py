"""
최소 동전으로 돈을 거슬러 주는 함수를 Greedy Algorithm으로 구현해 보겠습니다.

우리가 작성할 함수 min_coin_count는 거슬러 줘야 하는 총액 value와 동전 리스트 coin_list를 파라미터로 받고, 거슬러 주기 위해 필요한 최소 동전 개수를
리턴합니다.

예를 들어 1170원을 거슬러 주기 위해서는 500원 2개, 100원 1개, 50원 1개, 10원 2개를 줄 수 있기 때문에 6을 리턴하면 되겠죠?

동전의 조합은 항상 500원, 100원, 50원, 10원이라고 가정합시다.
"""

def min_coin_count(value, coin_list):
    # 코인 리스트 복사, 정렬, 코인 갯수 초기화
    using_coin_list = coin_list.copy()
    coin_count = 0
    using_coin_list.sort()

    # print("current coin_list: ", using_coin_list)
    # 거스름 돈 갯수 구하기
    while len(using_coin_list) > 0:
        div_coin = using_coin_list.pop()
        # print("current div_coin: ", div_coin)
        cur_count = value // div_coin
        # print("current cur_count: ", cur_count)
        coin_count += cur_count
        value -= div_coin * cur_count
        # print("current length list: ", len(using_coin_list))

    # print("final coin count: ", coin_count)

    return coin_count
    # 코드를 작성하세요.

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))