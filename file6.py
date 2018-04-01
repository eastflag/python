with open('c:\Log\sample1.csv', 'r', newline='') as filereader:
    header = filereader.readline()
    print(header)
    header = header.strip()
    print(header)

    header_list = header.split(',')
    print(header_list)
    print(','.join(map(str, header_list)) + '\n')