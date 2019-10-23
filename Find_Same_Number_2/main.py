def find_same_number(some_list, start = 1, end = None):
    # 필요한 경우, start와 end를 옵셔널 파라미터로 만들어도 됩니다.
    # 코드를 쓰세요

    # 원소가 하나인 경우(찾았다)
    if start == end:
        return start

    if end == None:
        end = len(some_list) - 1

    mid = (start + end) // 2
    print("current mid: ", mid)
    # 범위 내 숫자의 갯수를 저장하는 변수
    # 차례대로 왼쪽과 오른쪽을 나누어서 저장한다
    left_count = 0
    right_count = 0

    for element in some_list:
        if start <= element <= mid:
            left_count += 1
        elif mid + 1 <= element <= end:
            right_count += 1
    print("current left_count: ", left_count, "current right_count: ", right_count)
    # 왼쪽 갯수와 오른쪽 갯수의 차이에 따라 재귀적으로 다시 접근
    # 갯수가 많은 쪽이 중복된 원소가 존재하는 쪽임
    if left_count > right_count:
        return find_same_number(some_list, start, mid)

    else:
        return find_same_number(some_list, mid+1, end)



# 중복되는 수 ‘하나’만 리턴합니다.
# print(find_same_number([1, 4, 3, 5, 3, 2])) # 3
# print(find_same_number([4, 1, 5, 2, 3, 5])) # 5
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3])) # 3