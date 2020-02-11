import string


def count_words(line: str):

    cnt = dict()
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.split()

    for word in words:
        word = word.lower()
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1

    return cnt


def main():

    line = "oh what a day what a lovely day"
    count = count_words(line)

    print(count)


if __name__ == '__main__':
    main()
