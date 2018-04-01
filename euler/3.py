# 소수 구하기
def isPrimeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# 30의 소수는 2 * 15, 3 * 10, 5 * 6
# 작은수 부터 시작해서 증가시키면서 나누어 떨이면 몫이 소수인지 확인한다.

# 가장 큰 소수 구하기
def getMaxPrimeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            if isPrimeNumber(int(n/i)):
                return int(n/i)
    return None

# print(isPrimeNumber(6))
print(getMaxPrimeNumber(600851475143))
