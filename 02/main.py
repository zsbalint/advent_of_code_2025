TEST_INPUT = "input1.txt"
MAIN_INPUT = "input2.txt"

def read_input(input):
    file = open(input, 'r')
    data = file.readlines()
    splitdata = []
    for item in data:
        splitdata = item.split(",")       
    return splitdata

def processA(ranges):
    sum = 0
    for act_range in ranges:
        start_index, stop_index = act_range.split("-")
        start_index, stop_index = int(start_index), int(stop_index)
        for i in range(start_index, stop_index+1):
            # split every number in two
            i_string = str(i)
            i_length = len(i_string)
            if len(i_string) % 2 == 0: # only valid if the length of the number is even
                first, second = i_string[:i_length//2], i_string[i_length//2:]
                if first == second:
                    sum = sum + i
    return sum

def processB(ranges):
    sum = 0
    for act_range in ranges:
        start_index, stop_index = act_range.split("-")
        start_index, stop_index = int(start_index), int(stop_index)
        for i in range(start_index, stop_index+1):
            i_string = str(i)
            if i_string in (i_string + i_string)[1:-1]:
                sum = sum + i
    return sum

print("test input A: ",processA(read_input(TEST_INPUT)))
print("main input A: ",processA(read_input(MAIN_INPUT)))
print("test input B: ",processB(read_input(TEST_INPUT)))
print("main input B: ",processB(read_input(MAIN_INPUT)))