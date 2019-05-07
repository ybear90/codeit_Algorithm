def fib_tab(n):
    # 코드를 작성하세요.
    fib_memory = {1: 1, 2: 1}

    if n >= 3:
        for i in range(3, n + 1):
            fib_memory[i] = fib_memory[i - 1] + fib_memory[i - 2]

    return fib_memory[n]

# 테스트
# print(fib_tab(1))
# print(fib_tab(2))
# print(fib_tab(3))
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))