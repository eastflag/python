f = open("c:/Log/a.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    else:
        print(line)

f.close()