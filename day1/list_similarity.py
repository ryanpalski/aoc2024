from collections import defaultdict

def calculate_similarity_score(my_list: list, my_dict):
    sim_score = 0
    for num in my_list:
        sim_score += num * my_dict[num]
    
    return sim_score

def list_similarity():
    input_file = "day1/list_distance_puzzle_input.txt"
    left_list = []
    right_dict = defaultdict(int)
    with open(input_file, "r") as file:
        for line in file:
            inputs = line.split()
            left_list.append(int(inputs[0]))
            right_dict[int(inputs[1])] += 1

    return calculate_similarity_score(left_list, right_dict)

print(list_similarity())