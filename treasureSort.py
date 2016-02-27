from operator import itemgetter

f = open('treasure.txt', 'r+')
s = f.read()

l1 = s.splitlines()
# print(l1)
l2 = [x.split(';') for x in l1]
# print(l2)
for x in l2:
    x[1] = int(x[1][:-3])
    x[2] = int(x[2][3:])

l2 = sorted(l2, key = itemgetter(0))
l3 = sorted(l2, key = itemgetter(1))
# print(l3)
l4 = sorted(l3, key = itemgetter(2))

# for x in l4:
#     print(x)
# print('5gp' > '10gp')

for x in l4:
    x[1] = str(x[1]) + ' gp'
    x[2] = 'pg ' + str(x[2])


# for x in l4:
#     print(x)

len0 = max([len(x[0]) for x in l4])
len1 = max([len(x[1]) for x in l4])
len2 = max([len(x[2]) for x in l4])

# print(len0)
# print(len1)
# print(len2)

l5 = [x[0]+ ';' + x[1]+ ';' + x[2] for x in l4]
l6 = [x[0].ljust(len0 + 4) + x[1].rjust(len1) + '    ' + x[2].ljust(len2) for x in l4]


# for x in l5:
#     print(x)

# f.write('this is a test\n')

f.close()

f = open('treasure.txt', 'w')
for x in l5:
    f.write(x+'\n')
f.close()

g = open('sortedTreasure.txt', 'w')
for x in l6:
    g.write(x+'\n')
g.close()
