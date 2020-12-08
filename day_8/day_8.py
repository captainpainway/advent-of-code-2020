import copy

puzzle_input = open("input.txt", "r")
lines = puzzle_input.read().strip().split("\n")

# ***Part 1***


def find_loop_value(lines):
    instructions = [tuple(x.split(" ")) for x in lines]
    acc = 0  # Accumulator
    indices = [0]  # List of visited indices.
    while True:
        idx = indices[-1]
        inst = instructions[idx]
        # Add current idx + instruction number
        if inst[0] == 'jmp':
            idx = idx + int(inst[1])
        # Add to the accumulator and increment idx by 1
        if inst[0] == 'acc':
            acc += int(inst[1])
            idx += 1
        # Increment idx by 1
        if inst[0] == 'nop':
            idx += 1
        # If the new idx is in the indices list,
        # that means we have a loop, so break
        # and return the acc.
        if idx in indices:
            return acc
        # If not broken, append to indices list.
        indices.append(idx)


print(find_loop_value(lines))

# ***Part 2***


# Brute force solution.
def fix_infinite_loop(lines):
    # Creating a list of instructions.
    instructions = [tuple(x.split(" ")) for x in lines]

    # Iterate over the length of the instruction list.
    # x will be the index of the instruction to change.
    for x in range(0, len(lines)):
        # Making a shallow copy of the instructions.
        inst_copy = copy.copy(instructions)
        val = inst_copy[x][1]  # Value of the instruction.
        # If the instruction at the index is 'jmp',
        # replace that instruction with 'nop' and the value.
        if inst_copy[x][0] == 'jmp':
            inst_copy[x] = ('nop', val)
        # If the instruction at the index is 'nop',
        # replace that instruction with 'jmp' and the value.
        elif inst_copy[x][0] == 'nop':
            inst_copy[x] = ('jmp', val)

        finished_program = find_correct_loop(inst_copy)
        if finished_program:
            # print(inst_copy[x])  # Check out the changed instruction.
            return finished_program


# Basically the same function as find_loop_value.
# Checks the index of the instruction to the length
# of the entire instruction list.
# If the index is >= that length, we're at the end.
def find_correct_loop(instructions):
    ins_length = len(instructions)
    acc = 0  # Accumulator
    indices = [0]  # List of visited indices.
    while True:
        idx = indices[-1]
        inst = instructions[idx]
        # Add current idx + instruction number
        if inst[0] == 'jmp':
            idx = idx + int(inst[1])
        # Add to the accumulator and increment idx by 1
        if inst[0] == 'acc':
            acc += int(inst[1])
            idx += 1
        # Increment idx by 1
        if inst[0] == 'nop':
            idx += 1
        # If the new idx is in the indices list,
        # that means we have a loop, so break
        # and return nothing.
        if idx in indices:
            return
        # This is where we break if the idx >=
        # the total length of the instruction list
        # and return the accumulated value.
        if idx >= ins_length:
            return acc
        # If not broken, append to indices list.
        indices.append(idx)


print(fix_infinite_loop(lines))
