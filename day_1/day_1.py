input = open("input.txt", 'r')
lines = input.readlines()

# Part 1
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
