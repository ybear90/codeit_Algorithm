"""
[1, 2, 5, 6, 7, 9, 11] 안에 합이 15가 되는 두 요소의 조합이 있는지 확인하고 싶습니다. 두 요소 6과 9의 합이 15가 되죠?

이 조합이 있는지 없는지를 알고 싶은 거죠.

함수 설명
함수 sum_in_list은 정수 search_sum와 정렬된 정수 리스트 sorted_list를 받아서 sorted_list안의 두 요소의 합이 search_sum가 되는 조합이 있는지

없는지를 불린으로 리턴합니다.

sum_in_list(15, [1, 2, 5, 6, 7, 9, 11])은 불린 True를 리턴합니다
"""

def sum_in_list(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while high > low:
        if sorted_list[low] + sorted_list[high] < search_sum:
            low += 1
        elif sorted_list[low] + sorted_list[high] > search_sum:
            high -= 1
        else:
            return True

    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))