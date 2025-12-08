TEST_INPUT = "input1.txt"
MAIN_INPUT = "input2.txt"

TEST_ITERATIONS = 10
MAIN_ITERATIONS = 1000

import math

def read_input(input):
    file = open(input, 'r')
    data = file.readlines()
    result = []
    for row in data:
        row2 = row.replace('\n', '')
        row3 = row2.split(',')
        row4 = [int(value) for value in row3]
        result.append(row4)
    return result

def connect_points(points_list, iterations):
    all_links = []
    for x in range(len(points_list)):
        for y in range(x+1, len(points_list)):
            all_links.append([x, y, math.dist(points_list[x], points_list[y])])
    all_links.sort(key=lambda row: row[2])

    return all_links[:iterations]

def create_circles(link_list):
    graph = {}
    for link in link_list:
        graph.setdefault(link[0], set()).add(link[1])
        graph.setdefault(link[1], set()).add(link[0])
        
    circuits = []
    visited = set()

    for node in graph:
        if node not in visited:
            stack = [node]
            component = set()
            
            while stack:
                n = stack.pop()
                if n not in visited:
                    visited.add(n)
                    component.add(n)
                    stack.extend(graph[n])
            
            circuits.append(component)

    circuits = sorted(circuits, key=lambda c: len(c), reverse=True)

    return(circuits)

def multiply_three_biggest(circuits):
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

def keep_connecting(points_list):
    full_links = connect_points(points_list, (len(points_list)*len(points_list)))
    # print(full_links)
    circles = create_circles(full_links[:5])
    current_link = 0
    while len(circles) > 1 or len(circles[0]) < len(points_list):
        current_link += 1
        circles = create_circles(full_links[:current_link])
        # print('last connection: ', full_links[current_link][0], ' and ' , full_links[current_link][1])
    num1 = points_list[full_links[current_link - 1][0]]
    num2 = points_list[full_links[current_link - 1][1]]
    
    return num1[0] * num2[0]
print(multiply_three_biggest(create_circles(connect_points(read_input(TEST_INPUT), TEST_ITERATIONS))))
print(multiply_three_biggest(create_circles(connect_points(read_input(MAIN_INPUT), MAIN_ITERATIONS))))

print(keep_connecting(read_input(TEST_INPUT)))
print(keep_connecting(read_input(MAIN_INPUT)))