f = open("c:/Log/a.txt", 'a')
for i in range(11, 21):
    data = "%d번째 입니다.\n" %i
    f.write(data)

f.close()