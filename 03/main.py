TEST_INPUT = "input1.txt"
MAIN_INPUT = "input2.txt"

def read_input(input):
    lines = []
    file = open(input, 'r')
    data = file.readlines()
    for row in data:
        row = row.replace('\n', '')
        lines.append(row)
    return lines


def find_joltage(lines):
    sum_joltage = 0
    for line in lines:
        max = 0
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                act_number = line[i] + line[j]
                if int(act_number) > max:
                    max = int(act_number)
        sum_joltage += max
    return sum_joltage

def find_joltage_b(lines):
    sum_joltage = 0
    for line in lines:
        removals = len(line) - 12       
        result = []
        for digit in line:
            while result and removals > 0 and result[-1] < digit:
                result.pop()
                removals -= 1
            result.append(digit)
        while removals > 0:
            result.pop()
            removals -= 1
        max_number = ''.join(result)
        # print(max_number, removals)
        sum_joltage += int(max_number)
    return sum_joltage



print('A test: ' + str(find_joltage(read_input(TEST_INPUT))))
print('A live: ' + str(find_joltage(read_input(MAIN_INPUT))))
print('B test: ' + str(find_joltage_b(read_input(TEST_INPUT))))
print('B live: ' + str(find_joltage_b(read_input(MAIN_INPUT))))