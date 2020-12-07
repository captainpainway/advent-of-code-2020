import re

puzzle_input = open("input.txt", "r")
test = puzzle_input.read()


# Found out about formatted string literals in Python.
# https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
# Basically turning the list into tuples of "container" and "contains",
# then recursively iterating over it to get the nesting-dolls of bags.
def find_shiny_golds(rules):
    container_list = [tuple(x.split(" contain ")) for x in rules.strip().split("\n")]
    all_possibles = set()

    # Have to remove the words "bag" and "bags" from the search results.
    # In the case of "1 bag" vs "bags", some bags aren't getting caught.
    def find_containers(bag_type):
        for cont in container_list:
            pattern = re.compile(rf"{bag_type}")
            contains = re.search(pattern, cont[1])
            if contains:
                all_possibles.add(cont[0][:-5])
                find_containers(cont[0][:-5])
    find_containers("shiny gold")
    return len(all_possibles)


print(find_shiny_golds(test))


def shiny_golds_contain(rules):
    container_list = [tuple(x.split(" contain ")) for x in rules.strip().split("\n")]
    container_dict = {k: v for k, v in container_list}

    # Look at me making a tree!
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.children = []

        def add_child(self, obj):
            self.children.append(obj)

    bag_tree = Node("1 shiny gold bag")  # Gold bag holds all

    # Make a tree of all the contents of the shiny gold bag.
    # If a child returns with "no other bags.", that's the end of that branch.
    def find_contains(bag_type, node_parent):
        bag_contains = container_dict[bag_type].split(", ")
        for c in bag_contains:
            if c == "no other bags.":
                break
            node = Node(c)
            node_parent.add_child(node)
            c = c.replace(".", "").replace("bags", "").replace("bag", "")
            find_contains(c[2:] + "bags", node)
    find_contains("shiny gold bags", bag_tree)

    total_bags = []

    # I felt like printing out the entire data tree with indents,
    # just so I could see what it looks like.
    def print_data_tree(node, indent):
        print(indent + node.data)
        indent += "    "
        for c in node.children:
            print_data_tree(c, indent)
    print_data_tree(bag_tree, '')

    # Multiply the number of bags with the number of parent bags
    # to get the total number of a bag within the gold bag.
    def add_bags(node, parent_bags):
        child_bags = int(node.data[0]) * parent_bags
        total_bags.append(child_bags)
        for c in node.children:
            add_bags(c, child_bags)
    add_bags(bag_tree, 1)

    # Sum all the bags except for the first node,
    # because that's the main shiny gold bag.
    return sum(total_bags[1:])


# example_input = open("example_input.txt", "r")
# example_test = example_input.read()
# print(shiny_golds_contain(example_test))

print(shiny_golds_contain(test))

# Super fail!
# I thought I could just find bags that contain shiny gold bags,
# but no, I need to recursively find the bags that contain
# THOSE bags as well!
def fail_shiny_golds(rules):
    pattern = re.compile(r'^[\w\s]+contain\s', flags=re.M)
    remove_containers = re.sub(pattern, '', rules)
    gold_pattern = re.compile(r'shiny gold', flags=re.M)
    shiny_gold = re.findall(gold_pattern, remove_containers)
    return len(shiny_gold)
