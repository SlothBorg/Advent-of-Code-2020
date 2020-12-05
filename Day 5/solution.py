def get_data():
    with open('data/input') as f:
        return f.read().splitlines()


def parse_boarding_pass(boarding_pass):
    rows = [*range(128)]
    columns = [*range(8)]
    for index, letter in enumerate(boarding_pass):
        if index < 7:
            rows = parse_row(rows, letter)
        else:
            columns = parse_column(columns, letter)
    return [rows[0], columns[0]]


def parse_row(rows, letter):
    if letter == 'B':
        rows = split_list(rows)
    elif letter == 'F':
        rows = split_list(rows, True)

    return rows


def split_list(list, lower=False):
    half = len(list) // 2
    if lower:
        return list[:half]
    else:
        return list[half:]


def parse_column(columns, letter):
    if letter == 'R':
        columns = split_list(columns)
    elif letter == 'L':
        columns = split_list(columns, True)

    return columns


def calc_seat_id(row, column):
    return row * 8 + column


def find_seat_id(ids):
    ids.sort()
    return [x for x in range(ids[0], ids[-1]+1) if x not in ids][0]


seat_ids = []
for boarding_pass in get_data():
    parsed_boarding_pase = parse_boarding_pass(boarding_pass)
    seat_ids.append(calc_seat_id(parsed_boarding_pase[0], parsed_boarding_pase[1]))

print(max(seat_ids))
print(find_seat_id(seat_ids))