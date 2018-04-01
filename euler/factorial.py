def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

# print(factorial(100))

sum = 0
for i in str(factorial(100)):
    sum += int(i)
print(sum)

# f(n) = n * f(n-1)
# n==1이면 1을 리턴 n면 f(n-1)