# f(n) = (n-2) + (n-1)

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n-1) + f(n-2)

n = 1
while True:
    k = f(n)
    n = n + 1
    len(str(k))
    if len(str(k)) > 1000:
        break

print(n)


