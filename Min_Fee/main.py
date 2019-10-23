def min_fee(pages_to_print):
    # 코드를 작성하세요.
    minimum_fee = 9999

    if len(pages_to_print) == 1:
        return pages_to_print[0]

    elif len(pages_to_print) == 0:
        return 0

    for i in range(len(pages_to_print)):
        # print("pages_to_print ith: ", pages_to_print[i], "current_length: ", len(pages_to_print))
        # temp_list = pages_to_print[:i] + pages_to_print[i+1:]
        # print("temp_list: ", temp_list)
        fee = pages_to_print[i] * len(pages_to_print) + min_fee(pages_to_print[:i] + pages_to_print[i+1:])
        # print("current_fee: ", fee, "current_length: ", len(pages_to_print))
        minimum_fee = min(minimum_fee, fee)

    # print("final minimum fee: ", minimum_fee)
    return minimum_fee


# 테스트
print(min_fee([6, 11]))
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
