from utilities import read_input
import numpy



def evaluate_if_hit_tree(row, y):
    """
    Read a row of information, and take in the current x and y position.
    If the x position is a #, return True because it is a tree.
    """
    print(f"Evaluating position {y} of row: {row}")
    print(f"Is this a tree?: {row[y]}")

    if row[y] == '.':
        return False

    elif row[y] == '#':
        return True

    else:
        raise ValueError


def get_y_position(row, y):
    """
    I need to handle when the y position is far greater
    than the length of the line.

    Instead of actually duplicating the text string, I use
    the modulo operator to figure out what position it loops back on
    itself to, since we know the string pattern is repeated
    """
    if y >= len(row):
        return y % len(row)

    else:
        return y


if __name__ == '__main__':

    lines = read_input('day3_input.txt')

    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    slope_tree_count = []

    for slope in slopes:

        tree_counter = 0
        x = 0
        y = 0

        for line in lines:
            print("="*20)
            print(f"{x}, {y}")

            if evaluate_if_hit_tree(
                    line,
                    get_y_position(line, y)
            ):
                print(f"Toboggan hits tree at {x, y}")
                tree_counter += 1

            y += slope[1]
            x -= slope[0]

        slope_tree_count.append(tree_counter)

    print(slope_tree_count)
    print(numpy.prod(slope_tree_count))