# https://adventofcode.com/2020/day/5

puzzle_input = open("input.txt", "r")
lines = puzzle_input.readlines()
lines = [line.strip() for line in lines]


# Create lists of rows and columns of seats.
# Based upon "F" or "B" split the list in half and return
# that half. Do the same with "L" and "R" with the columns.
def row_and_column(seat):
    row = seat[:-3]
    column = seat[7:]
    plane_rows = list(range(0, 128))
    plane_cols = list(range(0, 8))
    for r in row:
        split = len(plane_rows) // 2
        if r == "F":
            plane_rows = plane_rows[:-split]
        if r == "B":
            plane_rows = plane_rows[split:]
    row = plane_rows[0]
    for c in column:
        split = len(plane_cols) // 2
        if c == "L":
            plane_cols = plane_cols[:-split]
        if c == "R":
            plane_cols = plane_cols[split:]
    column = plane_cols[0]
    return row, column


# Return the seat ID of one seat based on
# row and column position.
def seat_id(seat):
    location = row_and_column(seat)
    return location[0] * 8 + location[1]


# Iterate over all of the seats and return
# the seat with the highest ID number.
# This is the answer to part 1.
def iterate_over_passes(lines):
    ids = [seat_id(line) for line in lines]
    return max(ids)


# Get all of the provided seat IDs.
# Then, sort the IDs from low to high.
# Next, get the range of possible IDs from lowest
# to highest, finally, loop over the range of possible
# IDs to see which one is missing from the list.
def my_seat(lines):
    ids = [seat_id(line) for line in lines]
    sorted_ids = sorted(ids)
    all_seats = list(range(sorted_ids[0], (sorted_ids[-1]) + 1))
    for (i, num) in enumerate(all_seats):
        if num != sorted_ids[i]:
            return num


print(iterate_over_passes(lines))
print(my_seat(lines))