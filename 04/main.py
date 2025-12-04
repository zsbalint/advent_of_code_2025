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

def map_padding(char, lines):
    line_length = len(lines[0])
    padded_map = []
    first_line = ['#']
    for i in range(line_length):
        first_line.append('#')
    first_line.append('#')

    padded_map.append(first_line)

    for line in lines:
        line_to_add = ['#']
        for char in line:
            line_to_add.append(char)
        line_to_add.append('#')
        padded_map.append(line_to_add)

    padded_map.append(first_line)

    return padded_map

def count_neighbors(map):
    height = len(map)
    width = len(map[0])

    result = 0
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            neighbor_piles = 0
            if map[y][x] == "@":
                if map[y-1][x-1] == "@":
                    neighbor_piles += 1
                if map[y-1][x] == "@":
                    neighbor_piles += 1
                if map[y-1][x+1] == "@":
                    neighbor_piles += 1
                if map[y][x-1] == "@":
                    neighbor_piles += 1
                if map[y][x+1] == "@":
                    neighbor_piles += 1
                if map[y+1][x-1] == "@":
                    neighbor_piles += 1
                if map[y+1][x] == "@":
                    neighbor_piles += 1
                if map[y+1][x+1] == "@":
                    neighbor_piles += 1
                
                if neighbor_piles < 4:
                    result += 1
    return result


def count_neighbors_recursive(removed, map, results):    
    result = results
    if removed:
        height = len(map)
        width = len(map[0])
        ### DEBUG
        # debug_map = []
        # for i in range(height):
        #     line = []
        #     for j in range(width):
        #         line.append(0)
        #     debug_map.append(line)
        # print(debug_map)
        ### DEBUG

        new_map = [['#' for _ in range(width)] for _ in range(height)]

        

        removed = False
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                new_map[y][x] = map[y][x]
                neighbor_piles = 0
                
                if map[y][x] == "@":
                    if map[y-1][x-1] == "@":
                        neighbor_piles += 1
                    if map[y-1][x] == "@":
                        neighbor_piles += 1
                    if map[y-1][x+1] == "@":
                        neighbor_piles += 1
                    if map[y][x-1] == "@":
                        neighbor_piles += 1
                    if map[y][x+1] == "@":
                        neighbor_piles += 1
                    if map[y+1][x-1] == "@":
                        neighbor_piles += 1
                    if map[y+1][x] == "@":
                        neighbor_piles += 1
                    if map[y+1][x+1] == "@":
                        neighbor_piles += 1
                    
                    if neighbor_piles < 4:
                        new_map[y][x] = '.'
                        neighbor_piles = 0
                        result += 1
                        removed = True
        ### DEBUG
        # for line in new_map:
        #     print(line, '\n')
        # print('\n')
        ### DEBUG
        # print(result)
        return count_neighbors_recursive(removed, new_map, result)
    
    else:
        return result


print(count_neighbors(map_padding('#', read_input(TEST_INPUT))))
print(count_neighbors(map_padding('#', read_input(MAIN_INPUT))))
print(count_neighbors_recursive(True, map_padding('#', read_input(TEST_INPUT)), 0))
print(count_neighbors_recursive(True, map_padding('#', read_input(MAIN_INPUT)), 0))