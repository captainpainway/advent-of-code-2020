import re
puzzle_input = open("input.txt", "r")
lines = puzzle_input.readlines()
lines = [line.strip() for line in lines]


def password_checker(passwords, method):
    reg = re.compile('(?P<num1>\d+)-(?P<num2>\d+)(\s)(?P<letter>\w)(:\s)(?P<password>\w+)')
    valid_passwords = 0
    for p in passwords:
        m = reg.match(p)
        password = m.group('password')
        letter = m.group('letter')
        n1 = int(m.group('num1'))
        n2 = int(m.group('num2'))
        if method == "part_1":
            instances = password.count(letter)
            if n1 <= instances <= n2:
                valid_passwords += 1
        elif method == "part_2":
            if len(password) < n2:
                return "The index is too high!"
            if (password[n1 - 1] == letter) != (password[n2 - 1] == letter):
                valid_passwords += 1
        else:
            return "Select a valid method: part_1 or part_2"
    return valid_passwords


print(password_checker(lines, "part_1"))
print(password_checker(lines, "part_2"))
