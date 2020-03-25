import nltk
nltk.download('punkt')

def normalize_sentences(paragraph):

    sentences = nltk.tokenize.sent_tokenize(paragraph)
    result = '  '.join([s.rstrip().lstrip() for s in sentences])
    return result


def main():
    print(normalize_sentences("I am. I was. I will be."))

    print(normalize_sentences("Hello? Yes, this is dog!"))


if __name__ == '__main__':
    main()
