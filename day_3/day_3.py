from functools import reduce

puzzle_input = open("input.txt", "r")
lines = puzzle_input.readlines()
lines = [line.strip() for line in lines]


# I want to find the index of each point in the array
# that is x * 3 from the previous line.
# Adding indices as (line number, index number) tuple.
# Also, have to modulo by the line length because
# each line repeats infinitely to the right.
def trees_encountered(tree_map):
    line_length = len(tree_map[0])
    input_length = len(tree_map)
    indices = [(x, (x * 3) % line_length) for x in range(0, input_length)]
    trees = [tree_map[l][i] for (l, i) in indices]
    number_of_trees = trees.count("#")
    return number_of_trees


print(trees_encountered(lines))


# Adding arguments for x, y coordinates (right, down).
# Fun little "ceiling division" trick https://stackoverflow.com/a/54585138.
# The y range has to be divided by the "down" amount.
def trees_encountered(tree_map, right, down):
    line_length = len(tree_map[0])
    input_length = len(tree_map)
    indices = [(x * down, (x * right) % line_length) for x in range(0, -(input_length // -down))]
    trees = [tree_map[l][i] for (l, i) in indices]
    number_of_trees = trees.count("#")
    return number_of_trees


# Takes the map of the slope and a list of slope tuples.
# Makes a list comprehension of each of the trees encountered.
# Then returns the product of each slope's trees.
def tree_product(tree_map, slopes):
    trees = [trees_encountered(tree_map, r, d) for (r, d) in slopes]
    return reduce(lambda a, b: a * b, trees)


print(tree_product(lines, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
