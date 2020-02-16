import argparse
import csv
from configparser import ConfigParser


def parse_arguments():
    parser = argparse.ArgumentParser(description='Converts .ini file into a .csv file.')

    parser.add_argument('input_file', help='The input .ini file', default=None, type=str)
    parser.add_argument('csv_file', help='The output .csv file', default=None, type=str)
    parser.add_argument('-c', '--collapsed', action='store_true')

    return parser.parse_args()


def main():
    args = parse_arguments()
    # print(args.input_file, args.csv_file)

    config = ConfigParser()
    config.read(args.input_file)

    if args.collapsed:
        rows = [
            {'header': name, **section}
            for name, section in config.items()
            if section
        ]

        with open(args.csv_file, 'w', newline="") as o_file:
            csv_writer = csv.DictWriter(o_file, fieldnames=rows[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(rows)

    else:
        rows = [
            [name, key, value]
            for name, section in config.items()
            for key, value in section.items()
        ]

        with open(args.csv_file, 'w', newline="") as o_file:
            csv_writer = csv.writer(o_file)
            csv_writer.writerows(rows)


if __name__ == '__main__':
    main()
