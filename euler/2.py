# sum = 0
# first = 1
# second = 2
#
# while True:
#     if second >= 4000000:
#         break
#
#     if second % 2 == 0:
#         sum += second
#
#     new = first + second
#     first = second
#     second = new
#
# print(sum)

# 재귀함수 이용
# f(n) = (n-2) + (n-1)

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n-1) + f(n-2)

# print(f(4))

n = 1
count = 0
while True:
    k = f(n)
    print(k)
    if k % 2 == 0:
        count = count + k
    n = n + 1
    if k > 4000000:
        break

print(count)