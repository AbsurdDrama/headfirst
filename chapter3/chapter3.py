import os
import time

print(os.getcwd())

if os.path.exists('sketch.txt'):

    data = open('sketch.txt')
    for each_line in data:
        if each_line.find(':') != -1:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said : ', end='')
            print(line_spoken, end='')
            time.sleep(0.1)
    data.close()

else:
    print("Not exists sketch.txt file")