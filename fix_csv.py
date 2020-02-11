import sys
import re
import csv

def define_args(args):

    arg_string = ' '.join(args)
    arguments = dict()

    print(arg_string)

    # Source - target files:
    pat_csv = re.compile(r'[\w\-]+\.csv')
    filenames = re.findall(pat_csv, arg_string)
    # if len(filenames) == 2:
    arguments['source'] = filenames[0]
    arguments['target'] = filenames[1]
    # else:
    #     print('Wrong name of arguments!\nPlease, specify (only) source and target files names.')
    #     sys.exit(2)

    # key arguments:
    arguments['delimiter'] = "|"
    arguments['quote'] = "'"

    pat_delim = re.compile(r'\-\-in\-delimiter=(\S+)')
    delim = re.findall(pat_delim, arg_string)
    if delim:
        arguments['delimiter'] = delim[0]

    pat_quote = re.compile(r'\-\-in\-quote=(\S+)')
    quote = re.findall(pat_quote, arg_string)
    if quote:
        arguments['quote'] = quote[0]
    
    
    return arguments



def main(args):
    arguments = define_args(args)
    # print(arguments)
    # print(arguments['delimiter'])

    with open(arguments['source'], 'r') as source:
        csv_reader = csv.reader(source, delimiter = arguments['delimiter'])

        with open(arguments['target'], 'w') as target:
            csv_writer = csv.writer(target, quotechar=arguments['quote'])

            for line in csv_reader:
                print(line)
                csv_writer.writerow(line)







if __name__ == '__main__':
    main(sys.argv[1:])