puzzle_input = open("input.txt", "r")
lines = puzzle_input.readlines()
lines = [line.strip() for line in lines]


# Splits each line into component parts:
# min/max bounds, target letter, and password.
# Counts the number of instances of the letter in the password.
# Increments the # of valid passwords if instances
# is between max and min.
def part_1(passwords):
    valid_passwords = 0
    for p in passwords:
        sp = p.split(" ")
        policy = sp[0].split("-")
        min = int(policy[0])
        max = int(policy[1])
        letter = sp[1][0]
        password = sp[2]
        instances = password.count(letter)
        if max >= instances >= min:
            valid_passwords += 1
    return valid_passwords


print(part_1(lines))


# Splits each line into component parts:
# indices, target letter, and password.
# Checks to see if the target letter is at idx1 XOR idx2.
# Using XOR here because we only want to count if it
# occurs once.
def part_2(passwords):
    valid_passwords = 0
    for p in passwords:
        sp = p.split(" ")
        policy = sp[0].split("-")
        idx1 = int(policy[0]) - 1
        idx2 = int(policy[1]) - 1
        letter = sp[1][0]
        password = sp[2]
        if (password[idx1] == letter) ^ (password[idx2] == letter):
            valid_passwords += 1
    return valid_passwords


print(part_2(lines))
