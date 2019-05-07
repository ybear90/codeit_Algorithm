def fib_optimized(n):
    # 코드를 작성하세요.
    prev = 1
    curr = 1

    # Case 1 : n is 1 or 2
    if n < 3:
        return curr

    # Case 2 : else case
    for i in range(3, n + 1):
        temp = prev
        prev = curr
        curr = temp + curr

    return curr

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
