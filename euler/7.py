# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
#
# 이 때 10,001번째의 소수를 구하세요.

# 소수 구하기
def isPrimeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
number = 1

while True:
    number += 1
    if isPrimeNumber(number):
        count += 1
        if count == 10001:
            break

print(number)