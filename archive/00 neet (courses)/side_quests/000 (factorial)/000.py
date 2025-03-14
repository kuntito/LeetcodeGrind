def factorial(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 1: return 1

    memo[n] = n * factorial(n-1, memo)
    return memo[n]

def factorialII(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


res = factorial(12)
print(res)
