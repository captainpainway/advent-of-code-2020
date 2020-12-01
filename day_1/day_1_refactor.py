from itertools import combinations
from functools import reduce

input = open("input.txt", 'r')
lines = input.readlines()


# This makes part 1 faster by removing the second loop.
# It doesn't even loop through fully once.
# It checks to see if the current number x has been added to dictionary d
# as the difference between n and a previous number.
# If not, it adds n - x: x to d.
def find_two_entries(n):
    d = {}
    for line in lines:
        x = int(line)
        if x in d:
            print(x, d[x])
            return x * d[x]
        d[n - x] = x


print(find_two_entries(2020))


# Creates every 3-number combination with itertools.combinations,
# then finds the combo that adds up to n.
# https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/
def find_three_entries(n):
    nums = list(map(lambda x: int(x), lines))
    combos = list(combinations(nums, 3))
    for c in combos:
        if sum(c) == n:
            print(c)
            return c[0] * c[1] * c[2]


print(find_three_entries(2020))


# Multi-use function that can be used to find any number of combinations
# that add up to n. Returns the product of the combo.
def find_entries(n, num_entries):
    combos = list(combinations([int(x) for x in lines], num_entries))
    for c in combos:
        if sum(c) == n:
            print(c)
            return reduce(lambda a, b: a * b, c)


print(find_entries(2020, 2))
print(find_entries(2020, 3))
