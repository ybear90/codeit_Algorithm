"""
 해설 코드와 염라불량감자님의 코드는 모두 O(n)의 공간복잡도를 갖지만 아래와 같이 코드를 작성하게 되면 리스트 대신 정수 변수 2 개만을 사용해서

 알고리즘의 추가적 공간복잡도를 O(1)까지 줄일 수 있습니다.

 혹시 관심이 있으실 것 같애서 코드와 코멘트 첨가해서 답변드립니다. 코멘트가 너무 많아서 읽기 힘드실 수 있는 점 양해 부탁드립니다.
"""

def trapping_rain(buildings):
    total_height = 0 # 총 갇히는 비의 양을 담을 변수
    n = len(buildings)

    # 처음부터 올라가는 인덱스와 마지막에서 내려오는 인덱스를 담을 변수
    low = 0
    high = n - 1

    # low 인덱스 기준으로 왼쪽으로 가장 높은 건물 높이
    left_max = 0

    # high 인덱스 기준으로 오른쪽으로 가장 높은 건물 높이
    right_max = 0

    # 모든 인덱스에 쌓인 빗물량을 다 확인할 때까지 반복문을 돌린다
    while low <= high:
        # low 인덱스의 건물 높이보다 low 인덱스 기준 항상 오른쪽에 있는 high 인덱스의 건물 높이가 높거나 같으면,
        # 이미 low 인덱스의 오른쪽으로는 해당 인덱스 건물 높이보다 높은 건물이 있기 때문에
        # low 인덱스 기준 왼쪽의 가장 높은 건물 높이만 고려하면서 쌓이는 빗물의 양을 구할 수 있습니다
        # 반대의 경우(high 인덱스 건물 높이보다 low 인덱스 건물 높이가 높을 때)에도 똑같이 생각할 수 있습니다
        if buildings[low] < buildings[high]: # low 인덱스의 건물 높이가 high 인덱스 건물 높이보다 낮을 때
            if buildings[low] >= left_max:
                # 현재 인덱스의 건물 높이가 왼쪽으로 가장 낮은 건물 높이와 같거나 더 크기 때문에
                # 해당 인덱스에는 빗물이 담기지 않고 low 기준 왼쪽으로 가장 높은 건물만 업데이트시킨다
                left_max = buildings[low]
            else:
                # 현재 인덱스에 담기는 빗물을 총 빗물량에 더해준다
                total_height += left_max - buildings[low]
            low += 1 # low를 1 증가시키고 다시 반복문을 돌린다

        else: # high 인덱스의 건물 높이가 low 인덱스 건물 높이보다 낮을 때
            if buildings[high] > right_max: # high 인덱스의 건물 높이가 low 인덱스 건물 높이보다 낮을 때
                # 현재 인덱스의 건물 높이와 오른쪽으로 가장 낮은 건물 높이와 같거나 더 크기 때문에
                # 해당 인덱스에는 빗물이 담기지 않고 high 기준 오른쪽으로 가장 높은 건물만 업데이트시킨다
                right_max = buildings[high]
            else:
                # 현재 인덱스에 담기는 빗물을 총 빗물량에 더해준다
                total_height += right_max - buildings[high]
            high -= 1 # high를 1 감소시키고 다시 반복문을 돌린다

    return total_height