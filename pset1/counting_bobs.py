counter = 0

while s.find('bob') != -1:
    c = s.find('bob')
    s = s[c+1:]
    counter += 1

print('Number of times bob occurs is: ' + str(counter))

