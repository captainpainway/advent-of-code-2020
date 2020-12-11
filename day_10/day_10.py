from functools import reduce
from collections import Counter

example_puzzle_input = open("example_input.txt", "r")
example_lines = [int(x) for x in example_puzzle_input.read().strip().split("\n")]
puzzle_input = open("input.txt", "r")
lines = [int(x) for x in puzzle_input.read().strip().split("\n")]

# *** Part 1 ***


# Sort the adapters from lowest to highest,
# add the port (0) and device (highest + 3) to the list.
# Get the differences between each adapter.
# Count up the 1 and 3 jolt differences, and multiply.
def all_the_adapters(data):
    largest = max(data)
    sorted_data = sorted(data)
    sorted_data.append(largest + 3)
    sorted_data.insert(0, 0)
    diffs = [b - a for a, b in zip(sorted_data[:-1], sorted_data[1:])]
    counts = {1: diffs.count(1), 3: diffs.count(3)}
    return counts[1] * counts[3]


# print(all_the_adapters(example_lines))
print(all_the_adapters(lines))

# *** Part 2 ***


# Different lengths of "1" jumps have a specific number of combos.
# "1111" has 7 different paths.
# "111" has 4 different paths.
# "11" has 2 different paths.
# Jumps of "1" and "3" only have 1 path.
def adapter_counting(data):
    largest = max(data)
    sorted_data = sorted(data)
    sorted_data.append(largest + 3)
    sorted_data.insert(0, 0)
    diffs = "".join([str(b - a) for a, b in zip(sorted_data[:-1], sorted_data[1:])])
    diffs = diffs.replace('1111', '7').replace('111', '4').replace('11', '2').replace('3', '').replace('1', '')
    return reduce(lambda a, b: a * b, [int(i) for i in diffs])


# print(adapter_counting(example_lines))
print(adapter_counting(lines))


# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfbo61q/
# How does this work?
def count_configurations(data):
    largest = max(data)
    sorted_data = sorted(data + [0])
    counts = Counter({0: 1})
    for n in sorted_data:
        for x in range(1, 4):
            counts[n + x] += counts[n]

    return counts[largest]


# print(count_configurations(example_lines))
print(count_configurations(lines))


# Recursion takes way too long,
# but I did make a nice tree.
# Works for smaller numbers like the example.
def adapter_configurations(data):
    largest = max(data)
    sorted_data = sorted(data)
    sorted_data.append(largest + 3)

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.children = []

        def add_child(self, obj):
            self.children.append(obj)

    adapter_tree = Node(0)

    def create_tree(arr, parent):
        for n in arr:
            if 0 < n - parent.data <= 3:
                node = Node(n)
                parent.add_child(node)
                create_tree(arr[1:], node)
    create_tree(sorted_data, adapter_tree)

    # Got this from https://stackoverflow.com/a/47882036
    def get_tree_paths(node):
        if len(node.children) == 0:
            return [[node.data]]
        return [
            [node.data] + path for child in node.children for path in get_tree_paths(child)
        ]

    print(get_tree_paths(adapter_tree))
    return len(get_tree_paths(adapter_tree))

# print(adapter_configurations(example_lines))
# print(adapter_configurations(lines))
