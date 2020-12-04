import re

def get_data():
    with open('data/input') as f:
        return f.read().split('\n\n')


def parse_passport(dirty_passport):
    passport = dirty_passport.split()
    return [fields.split(':') for fields in passport]


def validate_passport_fields(passport_fields, requirements):
    field_count = 0
    for field in passport_fields:
        if field[0] in requirements:
            field_count +=1
    return field_count >= 7


def validate_passport_data(passport_data, requirements):
    for data in passport_data:
        if data[0] == 'cid':
            pass
        elif re.search(requirements[data[0]], data[1]) == None:
            return False
    return True


passports = get_data()
field_requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports_with_valid_fields = 0
passports_with_valid_data = 0
data_requirements = {
    'byr' : '((^19[2-9]\d$)|((^200[0-2])$))',
    'iyr' : '(^(201\d$)|(^2020)$)',
    'eyr' : '(^(202\d$)|(^2030)$)',
    'hgt' : '(((1(([5-8]\d)|(9[0-3])))cm)|(((59)|(6\d)|(7[0-6]))in))',
    'hcl' : '#(\d|[a-f]){6}',
    'ecl' : '(amb|blu|brn|gry|grn|hzl|oth)',
    'pid' : '^\d{9}$'
}

for passport in passports:
    passport_data = parse_passport(passport)
    if validate_passport_fields(passport_data, field_requirements):
        passports_with_valid_fields += 1
        passports_with_valid_data += validate_passport_data(passport_data, data_requirements)

print(passports_with_valid_fields)
print(passports_with_valid_data)
