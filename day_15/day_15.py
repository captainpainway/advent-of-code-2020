example_input = open("example_input.txt", "r")
example_numbers = [int(x) for x in example_input.read().strip().split(",")]

puzzle_input = open("input.txt", "r")
numbers = [int(x) for x in puzzle_input.read().strip().split(",")]

# *** Part 1 ***


# Pretty simple, when the number already exists in the list,
# find the last index and subtract that from the current index
# and that is the next number. Else, the next number is 0.
def number_game(nums, turn):
    i = len(nums)
    while i < turn:
        if nums[-1] in nums[:-1]:
            last_idx = len(nums) - (nums[:-1][::-1].index(nums[-1]) + 1)
            nums.append(len(nums) - last_idx)
        else:
            nums.append(0)
        i += 1
    return nums[-1]


print(number_game(example_numbers, 2020))
print(number_game(numbers, 2020))

# *** Part 2 ***


# Using a dictionary to keep the last index of a number
# makes lookups much faster. Still takes a few seconds
# to run, though.
def number_game_2(nums, turn):
    i = len(nums)
    num_dict = {x: nums.index(x) + 1 for x in nums}
    while i < turn:
        num = nums[-1]
        if num in num_dict:
            last_idx = num_dict[num]
            nums.append(i - last_idx)
        else:
            nums.append(0)
        num_dict[num] = i
        i += 1
    return nums[-1]


print(number_game_2(example_numbers, 30000000))
print(number_game_2(numbers, 30000000))
