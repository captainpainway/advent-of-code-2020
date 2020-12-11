example_puzzle_input = open("example_input.txt", "r")
example_lines = [x for x in example_puzzle_input.read().strip().split("\n")]

puzzle_input = open("input.txt", "r")
lines = [x for x in puzzle_input.read().strip().split("\n")]

# *** Part 1 ***


# Makes an array out of each seat surrounding the current seat
# and checks to see if there is >= 4 or 0 occupied seats
# and updates the seats as needed.
def occupied_seats(data):
    matrix = [list(x) for x in data]

    def switches(mtx):
        new_mtx = []
        for (i, x) in enumerate(mtx):
            new_row = []
            for (j, y) in enumerate(x):
                adjacent_seats = [
                    mtx[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else None,
                    mtx[i-1][j] if i-1 >= 0 else None,
                    mtx[i-1][j+1] if i-1 >= 0 and j+1 < len(x) else None,
                    mtx[i][j-1] if j-1 >= 0 else None,
                    mtx[i][j+1] if j+1 < len(x) else None,
                    mtx[i+1][j-1] if i+1 < len(mtx) and j-1 >= 0 else None,
                    mtx[i+1][j] if i+1 < len(mtx) else None,
                    mtx[i+1][j+1] if i+1 < len(mtx) and j+1 < len(x) else None
                ]
                if adjacent_seats.count("#") >= 4 and y == "#":
                    new_row.append("L")
                elif adjacent_seats.count("#") == 0 and y == "L":
                    new_row.append("#")
                else:
                    new_row.append(y)
            new_mtx.append(new_row)
        return new_mtx

    # Loops through permutations until we get the same
    # seating arrangement twice.
    def switch_loop(mtx, old_mtx):
        if mtx == old_mtx:
            return mtx
        else:
            return switch_loop(switches(mtx), mtx)
    final_mtx = switch_loop(switches(matrix), matrix)

    return sum(x.count("#") for x in final_mtx)


print(occupied_seats(example_lines))
print(occupied_seats(lines))

# *** Part 2 ***


# Inefficient and slow, but gets the job done.
# Same as above, but makes an array of arrays of every seat on the diagonal.
# Then it finds the first seat in each seat array.
# Then it counts the number of occupied seats and updates.
def occupied_seats_2(data):
    matrix = [list(x) for x in data]

    def switches(mtx):
        new_mtx = []
        for (i, x) in enumerate(mtx):
            new_row = []
            for (j, y) in enumerate(x):
                left = list(reversed(x[:j]))
                right = x[j+1:]
                up = [mtx[i-k][j] for k in range(1, i+1)]
                down = [mtx[k][j] for k in range(i+1, len(mtx))]
                up_left = list(filter(lambda g: g, [mtx[i-k][j-k] if j-k >= 0 else None for k in range(1, i+1)]))
                up_right = list(filter(lambda g: g, [mtx[i-k][j+k] if j+k < len(x) else None for k in range(1, i+1)]))
                down_left = list(filter(lambda g: g, [mtx[i+k][j-k] if j-k >= 0 else None for k in range(1, len(mtx)-i)]))
                down_right = list(filter(lambda g: g, [mtx[i+k][j+k] if j+k < len(x) else None for k in range(1, len(mtx)-i)]))
                directions = [left, right, up, down, up_left, up_right, down_left, down_right]
                first_seats = []
                for d in directions:
                    first_seat = [f for f in d if f != "."][0:1]
                    first_seats.append("".join(first_seat))

                if first_seats.count("#") >= 5 and y == "#":
                    new_row.append("L")
                elif first_seats.count("#") == 0 and y == "L":
                    new_row.append("#")
                else:
                    new_row.append(y)
            new_mtx.append(new_row)
        return new_mtx

    # Loops through permutations until we get the same
    # seating arrangement twice.
    def switch_loop(mtx, old_mtx):
        if mtx == old_mtx:
            return mtx
        else:
            return switch_loop(switches(mtx), mtx)
    final_mtx = switch_loop(switches(matrix), matrix)

    return sum(x.count("#") for x in final_mtx)


print(occupied_seats_2(example_lines))
print(occupied_seats_2(lines))
