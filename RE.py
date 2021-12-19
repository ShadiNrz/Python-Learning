import re
hand = open('regex_sum_1295573.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) < 1 :  continue
    # print(stuff)
    for n in stuff:
        num = int(n)
        numlist.append(num)
print(sum(numlist))

# import re #(very simple)
# print(sum([int(i) for i in (re.findall('[0-9]+',(open('regex_sum_42.txt','r').read())))]))
