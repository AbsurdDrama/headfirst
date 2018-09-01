import os
import time

print(os.getcwd())

if os.path.isfile('sketch.txt'):

    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said : ', end='')
            print(line_spoken, end='')
            time.sleep(0.1)
        except ValueError:
            pass
    data.close()

