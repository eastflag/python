f = open("c:/Log/a.txt", 'w')
for i in range(1, 11):
    data = "%d번째\n" %i
    f.write(data)
f.close()