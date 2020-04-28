import csv
from io import StringIO


def condense_csv(csv_text, id_name=None):
    groups = {}
    csv_reader = csv.reader(StringIO(csv_text))
    if id_name is None:
        [id_name, *other] = next(csv_reader)

    headers = {id_name: None}

    for id_, attribute, value in csv_reader:
        if id_ not in groups:
            groups[id_] = {id_name:id_}
        headers[attribute] = None
        groups[id_][attribute] = value

    rows = list(groups.values())
    print(rows)
    out_file = StringIO()
    writer = csv.DictWriter(out_file, fieldnames=headers.keys())
    writer.writeheader()
    writer.writerows(rows)
    return out_file.getvalue()


def main():
    print(condense_csv(open('songs.txt').read(), id_name='Track'))

if __name__ == '__main__':
    main()
