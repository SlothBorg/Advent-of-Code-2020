def get_data():
    with open('data/input') as f:
        return f.read().splitlines()


def parse_boarding_pass(boarding_pass):
    return boarding_pass.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')


def calc_row(rows):
    return int(rows[:7], 2)


def calc_column(columns):
    return int(columns[-3:], 2)


def calc_seat_id(row, column):
    return row * 8 + column


def find_seat_id(ids):
    ids.sort()
    return [x for x in range(ids[0], ids[-1]+1) if x not in ids][0]


seat_ids = []
for boarding_pass in get_data():
    parsed_boarding_pase = parse_boarding_pass(boarding_pass)
    seat_ids.append(calc_seat_id(calc_row(parsed_boarding_pase), calc_column(parsed_boarding_pase)))

print(max(seat_ids))
print(find_seat_id(seat_ids))
