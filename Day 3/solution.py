def get_data():
    with open('data/input') as f:
        return f.read().splitlines()


def map_path(path_data, slope=3, down=1):
    path_taken = ''

    for index, line in enumerate(path_data[::down]):
        path_taken = path_taken + line[index * slope % len(line)]
    return path_taken


map_data = get_data()
path = map_path(map_data)
print('Part 1: ' + str(path.count('#')))

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

trees_hit = 1
for slope in slopes:
    print('Calculating for slope: Right {}, down {}'. format(slope[0], slope[1]))
    path = map_path(map_data, slope[0], slope[1])
    print(path.count('#'))
    trees_hit *= path.count('#')

print('Part 2: ' + str(trees_hit))
