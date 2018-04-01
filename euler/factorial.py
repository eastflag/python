def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

print(factorial(3))

# f(n) = n * f(n-1)
# n==1이면 1을 리턴 n면 f(n-1)