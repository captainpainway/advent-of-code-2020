# https://adventofcode.com/2020/day/6

puzzle_input = open("input.txt", "r")
txt = puzzle_input.read().replace("\n\n", "---").replace("\n", '').strip()
lines = txt.split("---")


def individual_yes_answers(data):
    dups_removed = [set(line) for line in data]
    counts = [len(arr) for arr in dups_removed]
    return sum(counts)


print(individual_yes_answers(lines))


def total_yes_answers(data):
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


print(total_yes_answers(lines))
