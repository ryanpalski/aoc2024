import os

def get_list_distances(list1: list, list2: list):
    list1.sort()
    list2.sort()

    distance = 0
    for i in range(0, len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))

    return distance

def list_distance():
    input_file = "day1/list_distance_puzzle_input.txt"
    list1 = []
    list2 = []
    with open(input_file, "r") as file:
        for line in file:
            inputs = line.split()
            list1.append(inputs[0])
            list2.append(inputs[1])
    
    return get_list_distances(list1, list2)

print(list_distance())