"""
Divide and conquer의 방법이지만

시간 복잡도가 개선되지 않음...(해설참조)
"""

def power(x, y):
    if y == 1:
        return x
    elif y == 0:
        return 1

    one = power(x, y // 2)
    another = power(x, y - (y // 2))
    # divide
    return one * another
    # conquer


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))