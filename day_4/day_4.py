# https://adventofcode.com/2020/day/4

import re

puzzle_input = open("input.txt", "r")
lines = puzzle_input.readlines()
lines = [line.strip() for line in lines]


# Split the text file data chunks, split those by the delimiter ":",
# then put those into the dictionary and push to a list when a
# newline is found.
def passport_processor(passports):
    arr = []
    passport = {}
    for line in passports:
        split_line = line.split(" ")
        for l in split_line:
            split_data = l.split(":")
            if len(split_data) < 2:
                arr.append(passport)
                passport = {}
                break
            passport[split_data[0]] = split_data[1]
    arr.append(passport)  # Don't forget the final passport!
    return arr


# Check individual passports for pass/fail based on dict keys.
def passport_checker(passport):
    pass_check = "pass"
    if 'cid' not in passport:
        pass_check = "pass"
    if 'byr' not in passport:
        pass_check = "fail"
    if 'iyr' not in passport:
        pass_check = "fail"
    if 'eyr' not in passport:
        pass_check = "fail"
    if 'hgt' not in passport:
        pass_check = "fail"
    if 'hcl' not in passport:
        pass_check = "fail"
    if 'ecl' not in passport:
        pass_check = "fail"
    if 'pid' not in passport:
        pass_check = "fail"
    return pass_check, passport


# Validation statements
# Since the final function only counts "pass",
# I'm using fail1, fail2, etc for debugging purposes.
def passport_validation(passport):
    if not passport['byr'].isdecimal():
        return "fail1"
    if not 1920 <= int(passport['byr']) <= 2002:
        return "fail2"
    if not passport['iyr'].isdecimal():
        return "fail3"
    if not 2010 <= int(passport['iyr']) <= 2020:
        return "fail4"
    if not passport['eyr'].isdecimal():
        return "fail5"
    if not 2020 <= int(passport['eyr']) <= 2030:
        return "fail6"
    if ("cm" not in passport['hgt']) and ("in" not in passport['hgt']):
        return "fail7"
    if "cm" in passport['hgt']:
        hgt = re.sub('\D', '', passport['hgt'])
        if not 150 <= int(hgt) <= 193:
            return "fail8"
    if "in" in passport['hgt']:
        hgt = re.sub('\D', '', passport['hgt'])
        if not 59 <= int(hgt) <= 76:
            return "fail8"
    if not re.match('^#[a-f0-9]{6}$', passport['hcl']):
        return "fail9"
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    eye_match = False
    for e in eye_colors:
        if passport['ecl'] == e:
            eye_match = True
            break
    if not eye_match:
        return "fail10"
    if not re.match('^[0-9]{9}$', passport['pid']):
        return "fail11"

    return "pass"


# Run through all passports in the file
# and report back the number of "pass" passports.
def check_all_passports(passports, validate):
    checked_passports = [passport_checker(p) for p in passport_processor(passports)]
    passed = list(map(lambda y: y[1], (filter(lambda x: x[0] == "pass", checked_passports))))
    if validate:
        validated_passports = [passport_validation(p) for p in passed]
        return validated_passports.count("pass")
    else:
        return len(passed)


print(check_all_passports(lines, False))
print(check_all_passports(lines, True))
