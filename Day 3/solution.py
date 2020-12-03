def get_data():
    with open('data/input') as f:
        return f.read().splitlines()


def map_path(path_data, slope=3):
    path_taken = ''

    for index, line in enumerate(path_data):
        path_taken = path_taken + line[index * slope % len(line)]
    return path_taken


map_data = get_data()
path = map_path(map_data)
print('Part 1: ' + str(path.count('#')))
