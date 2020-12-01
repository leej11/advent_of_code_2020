import itertools
from typing import List
from functools import reduce

def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        input_list = [int(line.rstrip()) for line in f]

    return input_list

def check_sum_equals_2020(inputs: List[int]):
    """
    Return boolean if x and y sum to 2020
    """
    if sum(inputs) == 2020:
        return True
    else:
        return False

def generate_all_pairwise_combinations(input_list, combination):
    """
    Get all combinations of the numbers in the list
    """
    return list(itertools.combinations(input_list,combination))


if __name__ == "__main__":
    input_list = read_input("day1_input.txt")
    print(input_list)

    combs_list = generate_all_pairwise_combinations(input_list, 3)
    print(combs_list)

    # Iterate over all the combinations, and print the combination that sums to
    # 2020.
    # Then perform the multiplication for that combination
    for i in combs_list:
        if check_sum_equals_2020(i):
            print(f"The combination is: {i}")
            print(f"The multiplication is: {reduce(lambda x, y: x * y, i)}")
            break