def binary_search(element, some_list):
    # 코드를 작성하세요.
    start_idx = 0
    end_idx = len(some_list) - 1

    while True:
        mid_idx = (start_idx + end_idx) // 2
        if element < some_list[mid_idx]:
            if start_idx == mid_idx:
                return None
            end_idx = mid_idx - 1
        elif element == some_list[mid_idx]:
            return mid_idx
        else:
            if end_idx == mid_idx:
                return None
            start_idx = mid_idx + 1


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))