from operator import itemgetter

### Create file object from input file
f = open('treasure.txt', 'r+')
s = f.read()

### Parsing and splitting file into list objects for manipulation
### Lists are composed of [item (str), value (int), page (int)]. l2 is the final
### list of this step
l1 = s.splitlines()
# print(l1)
l2 = [x.split(';') for x in l1]
# print(l2)
for x in l2:
    x[1] = int(x[1][:-3])
    x[2] = int(x[2][3:])

### List l2 sorted and becomes l4
l2 = sorted(l2, key = itemgetter(0))
l3 = sorted(l2, key = itemgetter(1))
# print(l3)
l4 = sorted(l3, key = itemgetter(2))

### All lines with a single '#' and a space were used for testing.
# for x in l4:
#     print(x)
# print('5gp' > '10gp')

### Now sorted lists have their "value" and "page" integer values turned into
### strings with appropriate prefixes / suffixes (which were removed earlier)
for x in l4:
    x[1] = str(x[1]) + ' gp'
    x[2] = 'pg ' + str(x[2])


# for x in l4:
#     print(x)

### Maximum length (character-wise) of each item name, value, and page number
### parameters obtained
len0 = max([len(x[0]) for x in l4])
len1 = max([len(x[1]) for x in l4])
len2 = max([len(x[2]) for x in l4])

# print(len0)
# print(len1)
# print(len2)

### l5 retains original formatting and will overwrite treasure.txt
### l6 is formatted using the lengths obtained previously and will have an
### organized structure. It will be used to write sortedTreasure.txt.
l5 = [x[0]+ ';' + x[1]+ ';' + x[2] for x in l4]
l6 = [x[0].ljust(len0 + 4) + x[1].rjust(len1) 
      + '    ' + x[2].ljust(len2) for x in l4]


# for x in l5:
#     print(x)

# f.write('this is a test\n')

### Close file object
f.close()

### Reopen with truncating write permission and write in unformatted list l5
f = open('treasure.txt', 'w')
for x in l5:
    f.write(x+'\n')
f.close()

### Create sortedTreasure.txt using l6 which included formatting
g = open('sortedTreasure.txt', 'w')
for x in l6:
    g.write(x+'\n')
g.close()
