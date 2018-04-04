# 다음은 연속된 1000자리 숫자입니다 (읽기 좋게 50자리씩 잘라놓음).
# 여기서 붉게 표시된 71112의 경우 7, 1, 1, 1, 2 각 숫자를 모두 곱하면 14가 됩니다.
#
# 이런 식으로 맨 처음 (7 × 3 × 1 × 6 × 7 = 882) 부터 맨 끝 (6 × 3 × 4 × 5 × 0 = 0) 까지 5자리 숫자들의 곱을 구할 수 있습니다.
# 이렇게 구할 수 있는 5자리 숫자의 곱 중에서 가장 큰 값은 얼마입니까?

str = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

# print(str.replace('\n', ''))
x = str.replace('\n', '')


# x: 문자열, n: 인접 갯수
def f(x, n):
    list = []
    for i in range(0, len(x) - n):
        list.append(x[i:i+n])

    list2 = []
    for i in list:
        sum = 1
        for j in i:
            sum *= int(j)
        list2.append(sum)
    return max(list2)

print(f(x, 13))

# list2 = []
# for i in list:
#     sum = 1
#     for j in i:
#         sum *= int(j)
#     list2.append(sum)
#
# print(list2)
# print(max(list2))


