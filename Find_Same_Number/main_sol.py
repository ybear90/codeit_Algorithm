"""
반복문으로 리스트를 돌면서 요소를 하나씩 볼 때, 해당 요소를 이미 보았는지 어떻게 확인할 수 있을까요?

한 번 본 요소들을 어딘가에 저장하면 다음에 다시 보게 되면 알 수 있습니다

이미 나온 여러 개의 요소를 저장할 수 있는 방법이 무엇이 있을지 생각해보세요.

여러 개의 요소를 저장할 수 있는 도구는 리스트와 사전이 있는데요. 둘 중 어떤 것을 쓰는지 크게 중요하지는 않지만 사전을 사용해볼게요.

아래 리스트에 반복되는 요소가 있는지 확인하고 싶다고 생각해봅시다. 중복되는 요소를 담을 사전 elements_seen_so_far = {}가 있다고 가정하겠습니다.

[1, 2, 4, 2, 5, 3]

0 번 째 요소 1이 사전에 있는 key인지 확인합니다(이미 본 요소인지). 처음 보는 요소이기 때문에 사전에 추가해줍니다.
(elements_seen_so_far[1] = True)
1 번 째 요소 2도 마찬가지로 사전에 추가합니다.
2 번 째 요소 4도 마찬가지로 사전에 추가합니다.
3 번 째 요소 2는 elements_seen_so_far에 이미 있는 key기 때문에 2를 리턴합니다.
시간 복잡도는 가능한 요소의 조합들을 다 보는 O(n2)보다 효율적인 O(n)로 풀 수 있습니다.

코드로 써보세요!
"""

def find_same_number(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    elements_seen_so_far = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in elements_seen_so_far:
            return element

        # 해당 요소를 사전에 저장시킨다
        elements_seen_so_far[element] = True

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))