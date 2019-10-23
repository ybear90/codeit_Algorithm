'''
솔희는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다. 그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...

가능한 최대 수익을 리턴시켜 주는 함수 max_profit_memo를 Memoization 방식으로 작성해 보세요. max_profit_memo는 파라미터 세 개를 받습니다.

price_list: 개수별 가격이 정리되어 있는 리스트
count: 판매할 새꼼달꼼 개수
cache: 개수별 최대 수익이 저장되어 있는 사전
예를 들어 price_list가 [0, 100, 400, 800, 900, 1000]이라면,

새꼼달꼼 0개에 0원
새꼼달꼼 1개에 100원
새꼼달꼼 2개에 400원
새꼼달꼼 3개에 800원
새꼼달꼼 4개에 900원
새꼼달꼼 5개에 1000원

이렇게 가격이 책정된 건데요. 만약 솔희가 새꼼달꼼 5개를 판매한다면 최대로 얼마를 벌 수 있을까요?
'''


def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    if count < 2:
        return price_list[count]

    # cache에 저장된 값이 있다면 저장된 값을 바로 리턴한다.
    if count in cache:
        return cache[count]

    # 최대 수익 값을 계산하여 cache를 업데이트 한다.

    # 1 : 2 ~ 5개 판매 시, price_list에 있는 원소들을 같이 고려해서 최대의 판매 값을 찾는다
    if 1 < count < len(price_list):
        cnt = 1
        while cnt <= count // 2:
            if cnt == 1:
                cache[count] = max(max_profit_memo(price_list, count - cnt, cache) + max_profit_memo(price_list, cnt, cache),
                                   price_list[count])
            else:
                cache[count] = max(max_profit_memo(price_list, count - cnt, cache) + max_profit_memo(price_list, cnt, cache),
                                   price_list[count], cache[count])
            cnt += 1
    # 2 : 6개 이상 판매 부터
    elif count > len(price_list) - 1:
        cnt = 1
        while cnt <= count // 2:
            if cnt == 1:
                cache[count] = max_profit_memo(price_list, count - cnt, cache) + max_profit_memo(price_list, cnt, cache)
            else:
                cache[count] = max(max_profit_memo(price_list, count - cnt, cache) + max_profit_memo(price_list, cnt, cache),
                                   cache[count])
            cnt += 1

    # print("current cache: ", cache)
    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)

# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 0))
print(max_profit([0, 100, 400, 800, 900, 1000], 1))
print(max_profit([0, 100, 400, 800, 900, 1000], 2))
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
