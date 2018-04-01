# n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.
#
# 예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
# 여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.
#
# 100! 의 자리수를 모두 더하면 얼마입니까?

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