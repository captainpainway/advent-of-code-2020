example_puzzle_input = open("example_input.txt", "r")
example = example_puzzle_input.readlines()

puzzle_input = open("input.txt", "r")
puzzle = puzzle_input.readlines()


# The soonest bus is the one greater than but closest to the timestamp.
# Multiply each bus number by the ceiling division of the timestamp and bus.
# Find the bus by the index of the smallest time.
# Find the wait time my subtracting the timestamp from the smallest time.
# Return the product of the bus number and the wait time.
def find_soonest_bus(data):
    timestamp = int(data[0].strip())
    buses = [int(x) for x in data[1].split(",") if x.isdecimal()]
    times = [b * (-(timestamp // -b)) for b in buses]
    min_time = min(times)
    bus = buses[times.index(min_time)]
    wait_time = min_time - timestamp
    return bus * wait_time


print(find_soonest_bus(example))
print(find_soonest_bus(puzzle))


# Basically got the solution from here:
# https://old.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfr2uh6/
# I was originally looping through every number, which took forever.
# This solution jumps the increment up by the bus number after finding a timestamp
# that satisfies the (timestamp + offset) % bus requirement.
# By the time the last bus is calculated, the timestamp will satisfy all the requirements.
def find_subsequent_departures(data):
    arr = data[1].strip().split(",")
    bus_schedule = [(int(x), arr.index(x)) for x in arr if x.isdecimal()]
    timestamp = 0
    increment = 1
    for (bus, offset) in bus_schedule:
        while (timestamp + offset) % bus:
            timestamp += increment
        increment *= bus
    return timestamp


print(find_subsequent_departures(example))
print(find_subsequent_departures(puzzle))
