sum = 0
first = 1
second = 2

while True:
    if second >= 4000000:
        break

    if second % 2 == 0:
        sum += second

    new = first + second
    first = second
    second = new

print(sum)
