INPUTFILE = 'input2.txt'

file = open(INPUTFILE, 'r')
raw_content = file.readlines()

position = 50
count = 0

""" PART A 

for item in raw_content:
    item = item.replace('\n', '')
    direction, amount = item[0], int(item[1:])
    if direction == "L":          # turn left -> minus
        position -= amount
        while position < 0:
            position += 100
    elif direction == "R":     # turn right -> plus
        position += amount
    while position >= 100:
            position -= 100
    if position == 0:
        count += 1

print(count)

"""

#### PART B ####

for item in raw_content:
    item = item.replace('\n', '')
    direction, amount = item[0], int(item[1:])

    if direction == "L":        #turn left -> minus
        for i in range(amount):
            position -= 1
            if position == 0:
                count += 1
            if position == -1:
                position = 99

    elif direction == "R":
        for i in range(amount):
            position += 1
            if position == 100:
                position = 0
            if position == 0:
                count += 1



print(count)