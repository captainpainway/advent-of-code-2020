import re
example_puzzle_input = open("example_input.txt", "r")
example_puzzle = example_puzzle_input.readlines()

puzzle_input = open("input.txt", "r")
puzzle = puzzle_input.readlines()

# *** Part 1 ***


def process_input(data):
    data = [x.strip() for x in data]
    fields = data[:data.index("")]
    data = data[data.index(""):][1:]
    my_ticket = data[1:2]
    nearby_tickets = data[4:]
    return fields, my_ticket, nearby_tickets


def invalid_tickets(data):
    fields, my_ticket, nearby_tickets = process_input(data)
    fields = " ".join(fields)
    ranges = re.findall(r"(\d+-\d+)", fields)
    removes = set()
    for x in ranges:
        rng = x.split("-")
        rng = set(range(int(rng[0]), int(rng[1]) + 1))
        removes.update(rng)

    error_rate = 0
    for n in nearby_tickets:
        nums = set(int(i) for i in n.split(","))
        invalid_nums = nums - removes
        for i in invalid_nums:
            error_rate += i
    return error_rate


# print(invalid_tickets(puzzle))

# *** Part 2 ***


def remove_invalid_tickets(data):
    fields, my_ticket, nearby_tickets = process_input(data)
    fields = " ".join(fields)
    ranges = re.findall(r"(\d+-\d+)", fields)
    removes = set()
    for x in ranges:
        rng = x.split("-")
        rng = set(range(int(rng[0]), int(rng[1]) + 1))
        removes.update(rng)

    for n in nearby_tickets:
        nums = set(int(i) for i in n.split(","))
        invalid_nums = nums - removes
        if invalid_nums:
            nearby_tickets = [x for x in nearby_tickets if x != n]

    return nearby_tickets


def find_fields(data):
    fields, my_ticket, nearby_tickets = process_input(data)
    fields = dict(x.split(": ") for x in fields)

    my_ticket = [int(x) for x in my_ticket[0].split(",")]

    # Make a dictionary of ranges for each field
    for f in fields:
        ranges = re.findall(r"(\d+-\d+)", fields[f])
        valids = set()
        for r in ranges:
            rng = r.split("-")
            rng = set(range(int(rng[0]), int(rng[1]) + 1))
            valids.update(rng)
        fields[f] = valids

    valid_tickets = remove_invalid_tickets(data)

    # Make a dictionary of values at each index in
    # the valid tickets list
    columns = {}
    for v in valid_tickets:
        values = [int(x) for x in v.split(",")]
        for (i, c) in enumerate(values):
            if i in columns:
                columns[i].add(c)
            else:
                columns[i] = {c}

    # Compare sets of field ranges and columns
    potentials = {}
    for f in fields:
        for c in columns:
            diff = columns[c] - fields[f]
            if not diff:
                if f in potentials:
                    potentials[f].add(c)
                else:
                    potentials[f] = {c}

    for p in potentials:
        print(p, sorted(potentials[p]))

    # Did the column sorting by hand
    # See day_16_valid_indices.jpg
    # and day_16_field_sorting.jpg
    indices = [1, 2, 5, 8, 11, 15]
    product = 1
    for c in indices:
        product *= my_ticket[c]

    return product


print(find_fields(puzzle))
