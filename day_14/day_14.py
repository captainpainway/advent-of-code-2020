import re

example_puzzle_input = open("example_input.txt", "r")
example = example_puzzle_input.readlines()

puzzle_input = open("input.txt", "r")
puzzle = puzzle_input.readlines()

# *** Part 1 ***


# Save mask values as they appear in the list.
# Get the binary value for each address and pad to 36 digits.
# Anywhere mask != X, overwrite binary values with those values.
# Get the masked decimal number from the binary value.
# Save the number to the mem dictionary.
# Finally, add up all the values in the dictionary.
def bitmask(data):
    mem = {}
    data = [x.strip() for x in data]
    mask = ''
    for d in data:
        line = d.split(" = ")
        if line[0] == "mask":
            mask = list(line[1])
        else:
            binary = list(bin(int(line[1])).replace("0b", ""))
            while len(binary) < 36:
                binary.insert(0, '0')
            for (i, b) in enumerate(binary):
                if mask[i] != "X":
                    binary[i] = mask[i]
            binary = ''.join(binary)
            number = int(binary, 2)
            memslot = re.search(r"mem\[(\d+)\]", line[0])[1]
            mem[memslot] = number
    return sum(mem.values())


print(bitmask(example))
print(bitmask(puzzle))

# *** Part 2 ***


# Again, save mask values as they appear.
# Get the value from the mem lines, VALUE DOESN'T CHANGE!
# Get the binary value of the actual address and pad to 36 digits.
# Overwrite the binary address with X or 1 values from the mask.
# Run it through floating_bits to get all possible addresses.
# Iterate over all the possible addresses and save the value
# in each address to the mem dictionary.
# Sum all the values in the dictionary.
def bitmask_ver_2(data):
    mem = {}
    data = [x.strip() for x in data]
    mask = ''
    for d in data:
        line = d.split(" = ")
        if line[0] == "mask":
            mask = list(line[1])
        else:
            value = int(line[1])
            binary = list(bin(int(re.search(r"mem\[(\d+)\]", line[0])[1])).replace("0b", ""))
            while len(binary) < 36:
                binary.insert(0, '0')
            for (i, b) in enumerate(binary):
                if mask[i] == "X" or mask[i] == "1":
                    binary[i] = mask[i]
            binary = ''.join(binary)
            addresses = [int(x, 2) for x in floating_bits(binary)]
            for a in addresses:
                mem[a] = value
    return sum(mem.values())


# The number of possible addresses with be 2^n, where n is the number
# of X values in the address.
# Create a list of the incomplete addresses of 2^n length.
# Iterate over the addresses, and get the binary for i. Pad i to n places.
# For each X in the address, insert a corresponding digit of the i binary value.
# Join the address into a string and return the list of addresses.
def floating_bits(b):
    length = b.count("X")
    number_of_addresses = 2 ** length
    addresses = [b] * number_of_addresses

    for (i, a) in enumerate(addresses):
        binary = list(bin(i).replace("0b", ""))
        while len(binary) < length:
            binary.insert(0, '0')
        address = list(a)
        for r in range(0, length):
            address[address.index("X")] = binary[r]
        addresses[i] = ''.join(address)
    return addresses


print(bitmask_ver_2(example))
print(bitmask_ver_2(puzzle))
