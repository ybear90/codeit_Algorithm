def merge(list1, list2):
    merge_list = list()
    list1_copy = list1.copy()
    list2_copy = list2.copy()

    # If empty list is existed.
    if len(list1_copy) == 0 and len(list2_copy) == 0:
        return merge_list

    while len(list1_copy) != 0 or len(list2_copy) != 0:
        if len(list1_copy) == 0:
            while len(list2_copy) != 0:
                merge_list.append(list2_copy.pop(0))
            return merge_list
        elif len(list2_copy) == 0:
            while len(list1_copy) != 0:
                merge_list.append(list1_copy.pop(0))
            return merge_list

        while len(list1_copy) != 0 and len(list2_copy) != 0:
            if list1_copy[0] < list2_copy[0]:
                merge_list.append(list1_copy.pop(0))
            else:
                merge_list.append(list2_copy.pop(0))


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    # Split and merge sorted list
    return merge(merge_sort(my_list[:len(my_list) // 2]), merge_sort(my_list[len(my_list) // 2:]))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

# merge function 테스트
# print(merge([1], []))
# print(merge([], [1]))
# print(merge([2], [1]))
# print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
# print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
# print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
