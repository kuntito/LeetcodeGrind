def fibonacci(n, memo = {}):
    if n in memo: return memo[n]

    if n == 1: return 1
    if n < 1: return 0

    memo[n-1] = fibonacci(n-1)
    memo[n-2] = fibonacci(n-2)

    return memo[n-1] + memo[n-2]


def fibonacciII(n):
    memo = {
        0: 0,
        1: 1
    }

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


res = fibonacci(6)
print(res)