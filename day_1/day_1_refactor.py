from itertools import combinations
input = open("input.txt", 'r')
lines = input.readlines()


# This makes part 1 faster by removing the second loop.
def find_two_entries(n):
    d = {}
    for line in lines:
        x = int(line)
        d[n - x] = x
        if x in d:
            print(x, d[x])
            return x * d[x]


print(find_two_entries(2020))


# Creates every 3-number combination with itertools.combinations,
# then finds the combo that adds up to n.
def find_three_entries(n):
    nums = list(map(lambda x: int(x), lines))
    combos = list(combinations(nums, 3))
    for c in combos:
        if sum(c) == n:
            print(c)
            return c[0] * c[1] * c[2]


print(find_three_entries(2020))
