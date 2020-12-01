input = open("input.txt", 'r')
lines = input.readlines()

# Part 1
# Loops through the provided numbers
# and loops through all numbers before
# until finding the numbers that equal 2020.
for (i, line) in enumerate(lines):
    for j in range(0, i):
        a = int(line)
        b = int(lines[j])
        sums = a + b
        if sums == 2020:
            print(a, b)
            print(a * b)
            break

# Part 2
# The same as part 1, but with an additional loop
# that loops through the numbers again.
# Unless all the numbers are at the end of the list,
# this should be fast-ish as it breaks when 2020 is found.
for (i, line) in enumerate(lines):
    for j in range(0, i):
        for k in range(0, j):
            a = int(line)
            b = int(lines[j])
            c = int(lines[k])
            sums = a + b + c
            if sums == 2020:
                print(a, b, c)
                print(a * b * c)
                break
