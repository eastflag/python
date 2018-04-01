# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
#
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

# 에라토스체네스의 체 알고리즘 활용
import math

def eratos(n):
    primeList = []
    for i in range(2, n+1):
        primeList.append(True)


    for i in range(2, n+1):
        for j in range(2, int(math.sqrt(n)) + 1):
            if primeList[i-2] == False:
                break
            if i % j == 0 and i != j:
                primeList[i-2] = False

    # sum = 0
    # for i in list:
    #     if list[i]:
    #         sum += i +2
    # print(sum)
    return primeList

sum = 0
index = 0
for i in eratos(2000000):
    if i:
        sum += index + 2
    index += 1

# print(eratos(10))
print(sum)






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

