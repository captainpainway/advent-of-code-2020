example_puzzle_input = open("example_input.txt", "r")
example_lines = [x for x in example_puzzle_input.read().strip().split("\n")]

puzzle_input = open("input.txt", "r")
lines = [x for x in puzzle_input.read().strip().split("\n")]

# *** Part 1 ***


def ship_movements(data):
    directions = [(d[:1], int(d[1:])) for d in data]
    facing = "E"
    origin = (0, 0)
    location = (0, 0)

    # Jumps to the new direction based on the current facing
    # direction + the direction degrees divided by 90.
    def turns(dir):
        options = ["E", "S", "W", "N", "E", "S", "W", "N"]
        jumps = dir[1] // 90 if dir[0] == "R" else -dir[1] // 90
        return options[options.index(facing) + jumps]

    # Updates the location based on +x, -y positioning.
    def move(dir, amt, loc):
        if dir == "N":
            return loc[0], loc[1] + amt
        if dir == "S":
            return loc[0], loc[1] - amt
        if dir == "E":
            return loc[0] + amt, loc[1]
        if dir == "W":
            return loc[0] - amt, loc[1]

    # "F" direction moves in the "facing" direction.
    for d in directions:
        if d[0] == "R" or d[0] == "L":
            facing = turns(d)
        elif d[0] == "F":
            location = move(facing, d[1], location)
        else:
            location = move(d[0], d[1], location)

    # Manhattan distance.
    return abs(origin[0] - location[0]) + abs(origin[1] - location[1])


print(ship_movements(example_lines))
print(ship_movements(lines))

# *** Part 2 ***


def waypoint_movements(data):
    directions = [(d[:1], int(d[1:])) for d in data]
    origin = (0, 0)
    waypoint = (10, 1)
    location = (0, 0)

    # Rotating the waypoint around the ship is just
    # negating the coords in the case of 180,
    # or flipping both and negating one if rotation
    # is a quarter turn.
    def turns(dir, loc):
        deg = dir[1] if dir[0] == "R" else -dir[1]
        if abs(deg) == 180:
            return -loc[0], -loc[1]
        elif deg == 90 or deg == -270:
            return loc[1], -loc[0]
        elif deg == -90 or deg == 270:
            return -loc[1], loc[0]

    # Unchanged from the above function,
    # other than the name
    def move_waypoint(dir, amt, loc):
        if dir == "N":
            return loc[0], loc[1] + amt
        if dir == "S":
            return loc[0], loc[1] - amt
        if dir == "E":
            return loc[0] + amt, loc[1]
        if dir == "W":
            return loc[0] - amt, loc[1]

    # "F" now moves towards the waypoint from the current
    # location, multiplied by the number in the direction.
    for d in directions:
        if d[0] == "R" or d[0] == "L":
            waypoint = turns(d, waypoint)
        elif d[0] == "F":
            location = location[0] + d[1] * waypoint[0], location[1] + d[1] * waypoint[1]
        else:
            waypoint = move_waypoint(d[0], d[1], waypoint)

    # Manhattan distance.
    return abs(origin[0] - location[0]) + abs(origin[1] - location[1])


print(waypoint_movements(example_lines))
print(waypoint_movements(lines))
