'''
n번째 피보나치 수를 찾아주는 함수 fib_memo을 작성해 보세요.

fib_memo는 꼭 memoization 방식으로 구현하셔야 합니다!
'''
def fib_memo(n, cache):
    # 코드를 작성하세요.
    # (별해)
    # if n < 3:
    #     return 1
    if n == 1 or n == 2:
        cache[n] = 1
    # else:
    #     if len(cache) >= n - 1:
    #         cache[n] = cache[n - 1] + cache[n - 2]
    #     else:
    #         cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    # # print("fib_cache: ", cache)
    # return cache[n]
    # 논리적으로 어색함이 있어 해설을 참조하여 재작성
    # 이미 n번째 피보나치를 계산했으면
    # 저장된 값을 바로 리턴한다
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면:
    # 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {} # This data type is dictionary

    return fib_memo(n, fib_cache)


# 테스트
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(8))
# print(fib(9))

print(fib(10))
print(fib(50))
print(fib(100))