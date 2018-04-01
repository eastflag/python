#131
def jumin(jumin_number):
    result = jumin_number[7]
    if result == '1' or result == '3':
        return '남자입니다'
    elif result == '2' or result == '4':
        return '여자입니다.'
    else:
        return '알수없습니다'


print(jumin('700826-2709729'))

# 132
def comm(phone):
    number = phone[:3]
    if number == '010':
        return 'SKT'
    elif number == '016':
        return 'KTF'
    elif number == '019':
        return 'LGT'
    else:
        return 'none'

print(comm('019-3010-1482'))

# 133 문자열 역순 출력하기
def reverse_str(string1):
    result = ""
    for i in range(0, len(string1)):
        result += string1[len(string1)-1-i]
    return result

print(reverse_str("123 456 789"))

# 134
num = 3
def increase_num(num):
    num += 1
num = increase_num(num)
print(num)

# 135
mylist = [0, 1, 2]
def modify_list(mylist):
    mylist[0] = 100
modify_list(mylist)
print(mylist)

# 136
def add_str(string1, string2):
    return string1 + " " + string2
print(add_str("hello", "buddy"))

# 137
receipt = {'bread': 9900, 'fish': 15000, 'shampoo': 8000, 'soap': 2500, 'apple': 20000, 'banana': 3700}
for (k, v) in receipt:
    print(k, v)