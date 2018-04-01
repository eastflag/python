# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
#
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

# 소수 구하기
# 2 에서 n-2까지 나누기 =>
# n보다 작은 소수로 나누기
def f(n):
    primeList = [2]
    num = 3
    while (num <= n):
        for i in primeList:
            if num % i == 0:
                break
            elif i == primeList[-1]:
                primeList.append(num)

        num += 1
    return primeList

sum = 0
for i in f(2000000):
    sum += i

print(sum)