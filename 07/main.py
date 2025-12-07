TEST_INPUT = "input1.txt"
MAIN_INPUT = "input2.txt"

def read_input(input):
    file = open(input, 'r')
    data = file.readlines()
    result = []
    for row in data:
        row2 = row.replace('S', '|')
        row2 = [value for value in row2 if value != '\n']
        result.append(row2)
    return result

def calc_a(input):
    number_of_lines = len(input)
    line_length = len(input[0])
    splittings = 0
    for i in range(1, number_of_lines):
        for j in range(line_length):
            if input[i-1][j] == '|':
                if input[i][j] == '.':
                    input[i][j] = '|'
                elif input[i][j] == '^':
                    input[i][j-1] = '|'
                    input[i][j+1] = '|'
                    splittings += 1
    return splittings

def calc_b(input):
    number_of_lines = len(input)
    line_length = len(input[0])
    input[0] = [1 if x == '|' else x for x in input[0]]
    for i in range(1, number_of_lines):
        for j in range(line_length):
            if isinstance(input[i-1][j], int):                  # in this case numbers are used instead of '|', hence we have to check if the upper value is an integer
                if input[i][j] == '.':
                    input[i][j] = input[i-1][j]                 # if it's a dot, we simply copy the number from above
                
                elif input[i][j] == '^':
                    if isinstance(input[i][j-1], int):          # if it's already a number, we have to add the number above to the value
                        input[i][j-1] += input[i-1][j]
                    else:                                       # if not a number, we just copy the value from above, as before
                        input[i][j-1] = input[i-1][j]

                    if isinstance(input[i][j+1], int):          # same for the right side
                        input[i][j+1] += input[i-1][j]
                    else:                                   
                        input[i][j+1] = input[i-1][j]
               
                elif isinstance(input[i][j], int):              # if there is already a number written here when the check gets here, it means that we have to add the number above, if possible
                    if isinstance(input[i-1][j], int):
                        input[i][j] += input[i-1][j]       


    lastline = [value for value in input[-1] if isinstance(value, int)]     # select only the numbers from the last line, return the sum
    return sum(lastline)

print(calc_a(read_input(TEST_INPUT)))
print(calc_a(read_input(MAIN_INPUT)))
print(calc_b(read_input(TEST_INPUT)))
print(calc_b(read_input(MAIN_INPUT)))