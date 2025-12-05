TEST_INPUT = "input1.txt"
MAIN_INPUT = "input2.txt"


def read_input(input):
    ranges_raw = []
    ranges = []
    ingredients = []
    file = open(input, 'r')
    data = file.readlines()
    for row in data:
        row = row.replace('\n', '')
        if "-" in row:
            ranges_raw.append(row)
        elif row:
            ingredients.append(int(row))

    for curr_range in ranges_raw:
        from_to = curr_range.split("-")
        ranges.append([int(from_to[0]), int(from_to[1])])
    
    return ranges, ingredients

def process_a(in_range, in_ingredient):
    ranges = in_range
    ingredients = in_ingredient


    good_ingredients = set()

    for ingr in ingredients:
        for curr_range in ranges:
            if ingr > curr_range[0] and ingr <= curr_range[1]:
                # print(ingr, " is in range ", curr_range[0], "-", curr_range[1])
                good_ingredients.add(ingr)
                continue
    
    return len(good_ingredients)

def overlap(range_a, range_b): # check if two ranges overlap 
    
    if range_b[0] < range_a[0] and range_b[1] >= range_a[0] - 1:
        return True, min(range_a[0], range_b[0]), max(range_a[1], range_b[1])
    elif range_b[0] >= range_a[0] and range_b[1] <= range_a[1]:
        return True, range_a[0], range_a[1]
    elif range_b[1] > range_a[1] and range_b[0] <= range_a[1] + 1:
        return True, min(range_a[0], range_b[0]), max(range_a[1], range_b[1])
    elif range_b[0] <= range_a[0] and range_b[1] >= range_a[1]:
        return True, range_b[0], range_b[1]
    else:
        return False, -1, -1
    
def merge_overlaps(overlap_in, range_list):
    overlapping = overlap_in
    current_list = range_list
    # print(current_list)
    if overlapping:
        overlapping = False
        list_length = len(current_list)
        for i in range(list_length):
            for j in range(i+1, list_length):
                try:
                    overlapping_res, range_min, range_max = overlap(current_list[i], current_list[j])
                    if overlapping_res:
                        # print('overlap found')
                        overlapping = True
                        # print('overlapping ranges are ', current_list[i], ' and ', current_list[j])
                        current_list[i][0] = range_min
                        current_list[i][1] = range_max
                        current_list.pop(j)
                        list_length -= 1
                except:
                    pass
        return merge_overlaps(overlapping, current_list)
    else:
        return current_list

    

def process_b(in_range, nthng):
    ranges = in_range
    merged_list = merge_overlaps(True, ranges)   

    result = 0

    for ranges in merged_list:
        result = result + (ranges[1] - ranges[0] + 1)
    
    return result

print(process_a(*read_input(TEST_INPUT)))
print(process_a(*read_input(MAIN_INPUT)))
print(process_b(*read_input(TEST_INPUT)))
print(process_b(*read_input(MAIN_INPUT)))