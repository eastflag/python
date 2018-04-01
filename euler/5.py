# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
#
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

# 최대공약수 알고르즘: 유클리드 호제법
def gcd(a, b):

    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

# 최소공배수 알고리즘
def lcm(a, b):
    return a*b/gcd(a,b)

# print(lcm(8, 12))

# 1- 20 으로 모두 나누어지는 수 : 1-20의 최소 공배수 찾기
x = 2
for i in range (3, 21):
    x = lcm(x, i)
print(x)
