# 문자열과 튜플은 immutable
a = 'Life is too short'
print(a[3:-1])
print(len(a))
print(a.count('o'))
# x가 처음 나온 위치 만일 없다면 -1을 리턴
print(a.find('x'))
# b가 처음 나온 위치 만일 없으면 에러 발생
print(a.index('s'))

# 문자열 공백 지우기
print(a.strip())

print(a.split())

# formatting
# 왼쪽 정렬, 오른쪽 정렬, 가운데 정렬
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:#^10}".format("hi"))

print(a[-2])