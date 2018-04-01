# def beef():
#     print('This is function')
#
# def bitcoin_to_usd(btc):
#     amount = btc * 525
#     print(amount)
#
# bitcoin_to_usd(1)
# bitcoin_to_usd(2)

# default 값 지정
def dumb(name='dongkee', item='math'):
    print(name, item)

dumb()
# 뒷 부분 파라메터 호출 방법
dumb(item='english')

# flexible parameter
def count_number(*args):
    total = 0
    for x in args:
        total += x
    print(total)

count_number(1)
count_number(1, 2)
count_number(1, 2, 3)
print('--------------------------')

# unpacked arguments
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

buckys_data = [27, 20, 0]
health_calculator(*buckys_data)
