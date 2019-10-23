"""
Brute Force로 가능한 모든 조합들을 비교하는 방법도 있습니다. 하지만 너무 오래 걸리겠죠.

이 문제에는 최적 부분 구조와 탐욕적 선택 속성이 있기 때문에, Greedy Algorithm 방식으로 효율적이면서도 정확한 함수를 구현할 수 있습니다.

이 문제에서, 매 단계마다 가장 좋아 보이는 선택은 무엇일까요?

기다리는 시간을 최소화하기 위해서는, 페이지 수가 적은 사람 순으로 출력하면 됩니다. 즉, pages_to_print를 오름차순으로 정렬하면 된다는 거죠.

인풋 리스트 pages_to_print의 길이를 n이라고 합시다. 그러면 리스트를 정렬시켜 주는 부분이 O(nlgn)이고 for문 부분이 O(n)이죠?

합하면 O(nlgn+n)인데, 뒤에 있는 n을 생략할 수 있기 때문에 결국 시간 복잡도는 O(nlgn)입니다.
"""

def minimum_total_fee(pages_to_print):
    # 인풋으로 받은 리스트를 정렬시켜 준다
    sorted_list = sorted(pages_to_print)

    # 총 벌금을 담을 변수
    total_fee = 0

    # 정렬된 리스트에서 총 벌금 계산
    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)

    return total_fee


# 테스트
print(minimum_total_fee([3, 1, 4, 3, 2]))