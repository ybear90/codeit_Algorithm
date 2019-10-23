"""
Brute Force로 가능한 모든 조합들을 비교하는 방법도 있습니다. 하지만 너무 오래 걸리겠죠.

이 문제에는 최적 부분 구조와 탐욕적 선택 속성이 있기 때문에, Greedy Algorithm 방식으로 효율적이면서도 정확한 함수를 구현할 수 있습니다.

이 문제에서, 매 단계마다 가장 좋아 보이는 선택은 무엇일까요?

수강 신청 분석에서 보았듯, 가장 먼저 끝나는 수업을 선택하는 것이 최적의 선택입니다.

course_list를 가장 먼저 끝나는 순으로 정렬해야겠죠?

sorted 함수를 사용하면 정렬을 할 수 있는데, 어떻게 해야 우리가 원하는 기준으로 정렬할 수 있을까요?

모르시면 구글에 물어보세요

sorted 함수에 key 파라미터를 이용하면 원하는 기준으로 리스트를 정렬할 수 있습니다.

이제 겹치지 않게, 순서대로 수업을 선택하면 되겠네요.

이미 고른 수업이 끝나는 시간이 다른 수업이 시작하는 시간보다 늦으면, 두 수업은 겹친다고 볼 수 있습니다.

course_list의 길이를 n이라고 하면 정렬시키는 부분의 시간 복잡도는 O(nlgn)입니다. 그 후 반복문을 도는 부분은 O(n)이겠죠?

그럼 총 시간 복잡도는 O(nlgn+n)이기 때문에 결국 O(nlgn)이 되겠네요.
"""

def course_selection(course_list):
    # 수업을 끝나는 순서로 정렬한다
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        if course[0] >= my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))