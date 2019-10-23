def max_profit(price_list, count):
    # 코드를 작성하세요.
    # 최대의 이익 값을 저장하는 리스트 초기화
    profit_table = [0]

    # print("profit_table: ", profit_table)

    for i in range(1, count + 1):
        # print("current i: ", i)
        # profit 초기화
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0
        # print("current profit: ", profit)
        profit_table.append(profit)
        for j in range(1, i // 2 + 1):
            # print("current j: ", j)
            # count개를 팔 수 있는 조합들
            profit = max(profit, profit_table[i - j] + profit_table[j])
            # print("profit_table: ", profit_table)
        profit_table[i] = profit

    return profit_table[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
