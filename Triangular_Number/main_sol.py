"""
일단 재귀적인 호출을 제외하고 시간 복잡도를 생각해 봅시다. Base case의 시간 복잡도는 인풋 크기와 연관이 없으니까 O(1)입니다.

Recursive case에서는 triangle_number(n - 1)의 재귀적 호출을 제외하면 O(1)입니다.

그런데 재귀문을 통해서 triangle_number 함수는 총 n번 호출되니까, 총 O(n)의 시간이 걸리게 되죠.
"""

def triangle_number(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n + triangle_number(n - 1)

for i in range(1, 11):
    print(triangle_number(i))