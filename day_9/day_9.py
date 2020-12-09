example_puzzle_input = open("example_input.txt", "r")
example_lines = [int(x) for x in example_puzzle_input.read().strip().split("\n")]

puzzle_input = open("input.txt", "r")
lines = [int(x) for x in puzzle_input.read().strip().split("\n")]

# *** Part 1 ***


# Subtracts each number in the preamble by the following number
# at index p. This number is stored in the "sums" dictionary.
# If the number is already in the dictionary, that means that
# data[p] is a valid number. Call encryption_error recursively
# with the first number sliced off of the data list.
#
# If number i in the preamble is the same as the slice preamble[-1],
# that means we've reached the end of the preamble without finding
# a matching number, so the current number is invalid, return it.
def encryption_error(data, p):
    preamble = data[:p]
    target_num = data[p]
    sums = {}
    for i in preamble:
        if i in sums:
            # print(num, (i, sums[i]))
            data = data[1:]
            return encryption_error(data, p)
        elif i == preamble[-1]:
            return target_num
        else:
            sums[target_num - i] = i


print(encryption_error(lines, 25))

# *** Part 2 ***


# Use encryption_error to find the invalid number.
# First, filtering data to only use numbers smaller than the
# target number. Then, getting the sum of number d, end number
# data[i], and all numbers in-between.
#
# If total == num, return the sum of the smallest and largest numbers
# in the list.
def invalid_number_sum(data, num):
    data = [x for x in data if x < num]
    length = len(data)
    for (s, d) in enumerate(data):
        start = s + 1  # Start point for addition range.
        for i in range(start, length):
            end = i + 1
            total = d + sum(data[start:end])
            if total > num:
                break
            if total == num:
                return min(data[s:end]) + max(data[s:end])


# print(invalid_number_sum(example_lines, encryption_error(example_lines, 5)))
print(invalid_number_sum(lines, encryption_error(lines, 25)))
