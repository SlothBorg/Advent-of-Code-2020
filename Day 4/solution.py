def get_data():
    with open('data/input') as f:
        return f.read().split('\n\n')


def parse_passport(dirty_passport):
    passport = dirty_passport.split()
    return set([fields.split(':')[0] for fields in passport])


def validate_passport(passport, requirements):
    if len(passport) == 8:
        return True
    else:
        return all(elem in passport  for elem in requirements)


passports = get_data()
requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0
for passport in passports:
    valid_passports += validate_passport(parse_passport(passport), requirements)

print(valid_passports)
