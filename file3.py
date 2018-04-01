f = open("c:/Log/a.txt", 'r')

lines = f.readline()  # 한줄만 읽는다
# lines = f.readlines()   # 모든 라인을 읽어들이는데 배열로 읽는다.
# lines = f.read() # 모두 읽는다.

print(lines)
f.close()