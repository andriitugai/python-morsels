import os
from collections import defaultdict

def condense_csv(csv_string, id_name=None):
    matrix = defaultdict(dict)
    keys = []

    rows = iter(csv_string.splitlines())
    if id_name is None:
        id_name = next(rows).split(',')[0]

    for line in rows:
        id, key, value = line.split(',')
        if key not in keys:
            keys.append(key)
        matrix[id].update({key:value})

    result = id_name + ',' + ','.join([key for key in keys]) # header

    for id in matrix.keys():
        result += (os.linesep + id + ',' + ','.join([matrix[id].get(key, '') for key in keys]))

    return result



def main():
    print(condense_csv(open('songs.txt').read(), id_name='Track'))
    pass

if __name__ == '__main__':
    main()
