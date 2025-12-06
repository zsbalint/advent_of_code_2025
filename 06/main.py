TEST_INPUT = "input1.txt"
MAIN_INPUT = "input2.txt"

import numpy


def read_input(input):
    file = open(input, 'r')
    data = file.readlines()
    numbers = []
    for row in data:
        row = row.replace('\n', '')
        rowdata = row.split(' ')
        rowdata = [value for value in rowdata if value != '']
        if rowdata[0] in ('*', '+'):
            operators = rowdata
        else:
            numbers.append(rowdata)
    # print(numbers, operators)
    return numbers, operators

def read_input_b(input):
    file = open(input, 'r')
    data = file.readlines()
    numbers = []
    for row in data:
        row = row.replace('\n', '')
        if row[0] in ('*', '+'):
                rowdata = row.split(' ')
                rowdata = [value for value in rowdata if value != '']
                operators = rowdata
        else:
            numbers.append(row)
    # print(numbers, operators)
    input_length = len(numbers[0])
    numbers_count = len(numbers)

    vertical_numbers = []
    for i in range(input_length):
        act_number = ''
        for n in range(numbers_count):
            act_number = act_number + numbers[n][i]
        vertical_numbers.append(act_number)
    
    ### vertical_numbers now holds all the numbers read vertically, divided by elements consisting only of spaces.
    ### we have to split this list into smaller lists, using the whitespace-only elements as splitters

    result = []
    current = []

    for item in vertical_numbers:
        if item.strip() == '':
            if current:
                result.append(current)
                current = []
        else:
            current.append(item.strip())
    if current:
        result.append(current)
    # print(result, operators)
    return result, operators
        

def calculate_a(numbers, operators):
    result = 0
    for i in range(len(operators)):
        if operators[i] == '*':
            curr_result = 1
        else:
            curr_result = 0
        for num in numbers:
            # print(num, operands[i])
            if operators[i] == '*':
                curr_result = curr_result * int(num[i])
            else:
                curr_result = curr_result + int(num[i])
        result += curr_result
    return result

def calculate_b(numbers, operators):
    result = 0
    for i in range(len(operators)):
        if operators[i] == '*':
            curr_result = 1
        else:
            curr_result = 0
        for n in range(len(numbers[i])):
            if operators[i] == '*':
                curr_result = curr_result * int(numbers[i][n])
            else:
                curr_result = curr_result + int(numbers[i][n])
        result += curr_result
    return result

print(calculate_a(*read_input(TEST_INPUT)))
print(calculate_a(*read_input(MAIN_INPUT)))
print(calculate_b(*read_input_b(TEST_INPUT)))
print(calculate_b(*read_input_b(MAIN_INPUT)))