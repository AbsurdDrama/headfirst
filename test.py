# -*- coding: UTF-8 -*-
from chapter4.nester import print_lol

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing.')

print(man)
print(other)

with open("man_print_lol.txt", "w") as man_print_lol, open("other_print_lol.txt", "w") as other_print_lol:
    print_lol(man,fn=man_print_lol)
    print_lol(other,fn=other_print_lol)
