def trapping_rain(buildings):
    # 코드를 작성하세요
    # 1. 필요한 변수 설정
    water_mount = 0
    large_column = [-1, -1] # 왼쪽 값은 기둥 길이, 오른쪽 값은 기둥의 위치(초기화 값 : -1, -1)
    regular_column = [-1, -1] # 왼쪽 값은 기둥 길이, 오른쪽 값은 기둥의 위치(초기화 값: -1, -1)
    
    for i in range(len(buildings)):
        # 2. 기둥 생성(갱신까지 다 구현)
        if buildings[i] != 0:
            # 처음 대입 시에 넣을 조건
            if (large_column[0] == regular_column[0] == -1):
                large_column[0] = buildings[i]
                large_column[1] = i
            elif regular_column[0] <= buildings[i] <= large_column[0]:
                regular_column[0] = buildings[i]
                regular_column[1] = i
            elif large_column[0] <= buildings[i]:
                # Column swapping
                large_column[0], regular_column[0] = buildings[i], large_column[0]
                large_column[1], regular_column[1] = i, large_column[1]
            # Check Column Swapping
            print("Large column: ", large_column, "Regular column: ", regular_column)
        # 3. 물을 채울 수 있는지 판단 후 채우기(양쪽 벽이 생겨 있는지 판단 후 채우기, 리스트 인덱스의 위치도 고려)
        is_large_column = large_column[0] != -1 # 기둥의 유무 판단
        is_regular_column = regular_column[0] != -1 # 기둥의 유무 판단

        # 3-1. 칸막이가 제대로 쳐져있는지 확인하는 조건
        if (large_column[0] >= regular_column[0]) and (is_large_column == is_regular_column == True):
            if (large_column[1] > regular_column[1]):
                for k in range(regular_column[1] + 1, large_column[1]):
                    if buildings[k] < regular_column[0]:
                        # 실제 물 채우는 부분
                        while buildings[k] < regular_column[0]:
                            buildings[k] += 1
                            water_mount += 1       
            elif (large_column[1] < regular_column[1]):
                for k in range(large_column[1] + 1, regular_column[1]):
                    if buildings[k] < regular_column[0]:
                        while buildings[k] < regular_column[0]:
                            buildings[k] += 1
                            water_mount += 1

    # 채운 물의 양에 해당하는 변수 리턴(END)
    return water_mount

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))