def get_data():
    with open('data/input') as f:
        return f.read().split('\n\n')

def parse_answers(groups, strip=True):
    for index, group in enumerate(groups):
        groups[index] = group.replace('\n', '').strip()
    return groups

def calc_unique_answers(groups):
    answers = []
    for group in groups:
        answers.append(len(set(group)))
    return answers

group_answers = get_data()
answers = parse_answers(group_answers)
print("Solution 1: " + str(sum(calc_unique_answers(answers))))
