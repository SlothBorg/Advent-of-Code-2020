def get_data():
    with open('data/input') as f:
        return f.read().splitlines()


def parse_password_line(line):
    return line.replace('-', ' ').replace(':', '').split()


def is_valid_sled_password(line):
    count = line[3].count(line[2])

    if count >= int(line[0]) and count <= int(line[1]):
        return True
    else:
        return False


def is_valid_toboggan_password(line):
    if len(line[3]) < int(max(line[0], line[1])):
        print("Password too short")
        return False
    elif (line[3][int(line[0])-1] == line[2]) != (line[3][int(line[1])-1] == line[2]):
        return True
    else:
        return False


solution_1 = solution_2 = 0
for password in get_data():
    parsed_line = parse_password_line(password)
    if is_valid_sled_password(parsed_line):
        solution_1 += 1
    if is_valid_toboggan_password(parsed_line):
        solution_2 += 1

print('Solution 1: ' + str(solution_1))
print('Solution 2: ' + str(solution_2))
