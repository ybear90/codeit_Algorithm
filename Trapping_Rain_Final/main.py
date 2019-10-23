def trapping_rain(buildings):
    # 총 빗물에 대한 정의
    total_rain = 0

    # 끝 인덱스 정의
    end_index = len(buildings) - 1

    # 인덱스 기준으로 좌,우측 최대 높이 저장 리스트 정의
    # building 리스트의 길이 만큼 0으로 초기화
    left_height = [0] * len(buildings)
    right_height = [0] * len(buildings)

    # left_height, right_height 초기화
    left_height[0] = buildings[0]
    right_height[-1] = buildings[-1]

    for i in range(1, len(buildings)):
        left_height[i] = max(left_height[i - 1], buildings[i])

    for i in range(end_index - 1, -1, -1):
        right_height[i] = max(right_height[i + 1], buildings[i])

    # 빗물이 담길 수 있는 양을 계산
    for i in range(len(buildings)):
        possible_bound = min(left_height[i], right_height[i])

        # 빗물의 양은 0보다 작을 수 없다 차의 값이 0보다 작을 경우 0으로 치환
        total_rain += max(0, possible_bound - buildings[i])

    return total_rain


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))