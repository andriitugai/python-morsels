import os

def format_fixed_width(rows, padding=2, widths=None, alignments=None):
    if alignments is None:
        alignments = ['ljust'] * len(rows[0])
    else:
        alignments = [('ljust' if just == 'L' else 'rjust') for just in alignments]

    if widths is None:
        widths = [max([len(cell) for cell in column]) for column in [*zip(*rows)]]

    result = os.linesep.join(
        [
            ((padding*' ').join([getattr(cell, just)(width) for cell, width, just in zip(row, widths, alignments)])).rstrip()
            for row in rows
        ]
    )
    return result


def main():
    # print(format_fixed_width([['green', 'red'], ['blue', 'purple']]))
    rows = [['Robyn', 'Henry', 'Lawrence'], ['John', 'Barbara', 'Gross'], ['Jennifer', '', 'Bixler']]
    print(format_fixed_width(rows, alignments=['R', 'L', 'R']))
    print(format_fixed_width([["hi", "there"]]))


if __name__ == '__main__':
    main()

