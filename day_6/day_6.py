# https://adventofcode.com/2020/day/6

# Put each line into a set, get the length of the set,
# and sum the counts in the list.
def individual_yes_answers():
    puzzle_input = open("input.txt", "r")
    txt = puzzle_input.read().replace("\n\n", "---").replace("\n", '').strip()
    data = txt.split("---")
    dups_removed = [set(line) for line in data]
    counts = [len(arr) for arr in dups_removed]
    return sum(counts)


print(individual_yes_answers())


# Creating a dictionary of letters for each line.
# If any of the letters in the dictionary are equal to
# the length of the list created by splitting the line by
# spaces, it's considered a valid answer.
# Increment the number of valid answers by 1, and return that value.
def total_yes_answers():
    puzzle_input = open("input.txt", "r")
    txt = puzzle_input.read().replace("\n\n", "---").replace("\n", ' ').strip()
    data = txt.split("---")
    valid_answers = 0
    for line in data:
        dct = {}
        arr = line.split(" ")
        for answers in arr:
            letters = list(answers)
            for l in letters:
                if l in dct:
                    dct[l] += 1
                else:
                    dct[l] = 1
        for key in dct:
            if dct[key] == len(arr):
                valid_answers += 1
    return valid_answers


print(total_yes_answers())
