example_puzzle_input = open("example_input.txt", "r")
example = example_puzzle_input.readlines()
# example_lines = [x for x in example_puzzle_input.read().strip().split("\n")]

puzzle_input = open("input.txt", "r")
puzzle = puzzle_input.readlines()
# lines = [x for x in puzzle_input.read().strip().split("\n")]


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
