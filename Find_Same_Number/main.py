def find_same_number(some_list):
    duplicated_list = []
    for i in range(len(some_list)):
        duplicated_list.append(0)
    # print("current duplicated_list: ", duplicated_list)
    for value in some_list:
        # print("current duplicated_list: ", duplicated_list)
        if duplicated_list[value] == 1:
            return value
        duplicated_list[value] = 1


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2])) # 3
print("="*60)
print(find_same_number([4, 1, 5, 2, 3, 5])) # 5
print("="*60)
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3])) # 3