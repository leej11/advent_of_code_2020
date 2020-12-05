import re

def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        input_list = [line.rstrip() for line in f]

    return input_list


def get_evaluation_criteria(password):
    pattern = re.compile('(\d+)-(\d+)\s(\S): (\S+)')
    match_groups = pattern.match(password)

    evaluation_dict = {
        "iloc_1" : int(match_groups[1]),
        "iloc_2" : int(match_groups[2]),
        "letter" : match_groups[3],
        "password" : match_groups[4],
    }

    return evaluation_dict


def evaluate_password_against_criteria(iloc_1, iloc_2, letter,
                                       password):

    if (password[iloc_1 - 1], password[iloc_2 - 1]).count(letter) == 1:
        return True

    else:
        return False


if __name__ == "__main__":
    input_list = read_input("day2_input.txt")
    valid_counter = 0

    for input in input_list:
        print(f"Evaluating {input}")
        evaluation_dict = get_evaluation_criteria(input)

        if evaluate_password_against_criteria(**evaluation_dict):
            print("Password valid")
            valid_counter += 1

    print(f"Total # valid passwords: {valid_counter}")
