from itertools import product


class AlwaysTrue:
    def __eq__(self, other):
        return True


def sewer(toSew):
    if len(set(toSew)) == len(toSew):
        return toSew


def compare(first, second):
    forbidden_indexes = [[] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if first[i] == second[j]:
                forbidden_indexes[i].append(j)
    forbidden_indexes = delete_occurences(forbidden_indexes)
    if len(forbidden_indexes) == 4:
        return True
    return False


def delete_occurences(raw):
    almost_done = [[] for _ in range(4)]
    done = []
    for _ in range(4):
        for i in range(4):
            if len(raw[i]) == 1:
                almost_done[i].append(raw[i][0])
                for j in range(4):
                    try:
                        raw[j].remove(almost_done[i][0])
                    except ValueError:
                        pass
    for k in almost_done:
        done += k
    return done

def string_analyzer(string):
    final = ''
    flag = -1
    for i, s in enumerate(string):
        if s == '(' or s == ')' \
            or s == 'w' or s == 'x' or s == 'y' or s == 'z' \
                or s == '1' or s == '0':
            final += s
        elif s == '∨':
            final += ' or '
        elif s == '∧':
            final += ' and '
        elif s == '→':
            final += ' <= '
        elif s == '=' or s == '≡':
            final += ' == '
        elif s == '¬':
            if string[i+1] != '(':
                final += '(not '
                flag = i + 1
            else:
                final += 'not '
        if flag == i:
            flag = -1
            final += ')'
    return final

def main_algorithm(sentence, instances, str_amount):
    real_true = AlwaysTrue()
    acceptable = []
    try:
        for w in range(2):
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        if eval(string_analyzer(sentence)):
                            acceptable.append((w, x, y, z))
    except Exception:
        return 'Введённые данные некорректны.'

    full_instances = []
    input_columns = [[] for _ in range(4)]
    for i in range(str_amount):
        instance = tuple([instances[i][j][0] for j in range(4)])
        zeroes = instance.count(0)
        ones = instance.count(1)
        full_instances.append((instance, zeroes, ones))
        for j in range(4):
            if instance[j] == 2:
                input_columns[j].append(real_true)
            else:
                input_columns[j].append(instance[j])

    possible_instances = [[] for _ in range(len(full_instances))]
    for i in range(len(full_instances)):
        for t_instance in acceptable:
            t_zeroes = t_instance.count(0)
            t_ones = t_instance.count(1)
            if full_instances[i][1] <= t_zeroes and \
                    full_instances[i][2] <= t_ones:
                possible_instances[i].append(t_instance)

    possible_raws = []
    for kill in map(sewer, product(*possible_instances)):
        if kill is not None:
            possible_raws.append(kill)

    possible_column_sets = [
        [[] for p in range(4)] for q in range(len(possible_raws))
        ]
    for i in range(len(possible_raws)):
        for j in range(4):
            for k in range(len(full_instances)):
                possible_column_sets[i][j].append(possible_raws[i][k][j])

    winner = None
    for columns in possible_column_sets:
        if compare(columns, input_columns):
            winner = columns

    if winner is None:
        return 'Введённые данные некорректны.'

    letters = [[] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if winner[i] == input_columns[j]:
                if i == 0:
                    letters[j].append('w')
                elif i == 1:
                    letters[j].append('x')
                elif i == 2:
                    letters[j].append('y')
                else:  # i == 3:
                    letters[j].append('z')

    answer = delete_occurences(letters)

    return answer
