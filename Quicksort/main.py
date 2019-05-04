'''
Divide and Conquer 방식으로 quicksort 함수를 써 보세요. quicksort는 파라미터로 리스트 하나와 리스트 내에서 정렬시킬 범위를 나타내는
인덱스 start와 인덱스 end를 받습니다.
merge_sort 함수와 달리 quicksort 함수는 정렬된 새로운 리스트를 리턴하는 게 아니라, 파라미터로 받는 리스트 자체를 정렬시키는 것입니다.
'''

def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list

def partition(my_list, start, end):
    # Define variables
    back_idx = idx = start
    pivot = end

    # back_idx <= idx 이건 자명하므로 반복조건에 더하지 않는다
    while idx <= pivot:
        if my_list[idx] <= my_list[pivot]:
            swap_elements(my_list, back_idx, idx)
            back_idx += 1
            idx += 1
        elif my_list[idx] > my_list[pivot]:
            idx += 1

        if idx == pivot:
            swap_elements(my_list, back_idx, pivot)
            pivot = back_idx

    return pivot

def quicksort(my_list, start, end):
    # my_list size is only one
    if end - start < 1:
        return

    # Define mid variable
    pivot_index = partition(my_list, start, end)
    quicksort(my_list, start, pivot_index - 1)
    quicksort(my_list, pivot_index + 1, end)
    # quicksort(my_list, start, pivot_index - 1)
    # quicksort(my_list, pivot_index + 1, end)
    # pivot_index2 = partition(my_list, start, pivot_index - 1)
    # print(pivot_index2)
    #
    # pivot_index3 = partition(my_list, pivot_index + 1, end)
    # print(pivot_index3)


    # quicksort(my_list, start, pivot_index - 1)
    # quicksort(my_list, pivot_index + 1, end)




# swap_elements function test
# list1 = [1, 2, 3, 4, 5, 6]
# swap_elements(list1, 2, 5)
# print(list1)

# # 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
# bi, idx, piv = partition(list1, 0, len(list1) - 1)
# print(bi, idx, piv)
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
# list2 = [6, 1, 2, 6, 3, 5, 4]
# pivot_index2 = partition(list2, 0, len(list2) - 1)
# print(list2)
# print(pivot_index2)

# 테스트 1
# list1 = [1, 3, 5, 7, 9, 11, 13, 11]
# # # quicksort(list1, 0, len(list1) - 1)
# quicksort(list1, 0, len(list1) - 1)
# print(list1)
# #
# # # 테스트 2
# list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
# # quicksort(list2, 0, len(list2) - 1)
# quicksort(list2, 0, len(list2) - 1)
# print(list2)
#
# # 테스트 3
# list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
# # quicksort(list3, 0, len(list3) - 1)
# quicksort(list3, 0, len(list3) - 1)
# print(list3)

# # 테스트(부분) 1
# list4 = [30, 28, 48]
# quicksort(list4, 0, len(list4) - 1)
# print(list4)