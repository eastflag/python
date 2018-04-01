# 121
PI = 3.141592
print(round(PI*100)/100)

# 122
# https://pyformat.info/
price = 17730000
print('{:,d}'.format(price))

# 123
result1 = 78
print(bin(result1))
print('{:b}'.format(result1))

# 124 2진수 포맷해서 출력하기
def print_readable_bin(arg1):
    result = '{:b}'.format(arg1)
    print('_' + result + '_')

print_readable_bin(17)

# 125 two's complement

# 127
import os
os.system('python --version')

# 128
print(ord('A'))
print(chr(65))
