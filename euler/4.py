# 대칭수 확인하는 함수
def f(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

max = 0

# 3자리수 대칭수 구하기
for i in range(100, 1000):
    for j in range(100, 1000):
        k = i * j
        if f(k):
            if k >= max:
                max =k

print(max)