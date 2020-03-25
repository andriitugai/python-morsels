import unicodedata

class FuzzyString(str):

    @staticmethod
    def norma(text):
        return unicodedata.normalize("NFKD", text.casefold())

    def __contains__(self, item):
        return FuzzyString.norma(item) in FuzzyString.norma(self)

    def __add__(self, other):
        return FuzzyString(str(self) + other)

    def __eq__(self, other):
        if isinstance(other, str):
            return FuzzyString.norma(self) == FuzzyString.norma(other)

        return False

    def __ne__(self, other):
        if isinstance(other, str):
            return FuzzyString.norma(self) != FuzzyString.norma(other)

        return False

    def __gt__(self, other):
        if isinstance(other, str):
            return FuzzyString.norma(self) > FuzzyString.norma(other)

        return False

    def __ge__(self, other):
        if isinstance(other, str):
            return FuzzyString.norma(self) >= FuzzyString.norma(other)

        return False

    def __lt__(self, other):
        if isinstance(other, str):
            return FuzzyString.norma(self) < FuzzyString.norma(other)

        return False

    def __le__(self, other):
        if isinstance(other, str):
            return FuzzyString.norma(self) <= FuzzyString.norma(other)


def main():
    greeting = FuzzyString('Hey TREY!')
    # print(greeting == 'hey Trey!')

    o_word = FuzzyString('Octothorpe')
    print('OcTO_' in o_word)
    # print('Apple' < o_word)

    new_string = o_word + ' (aka hashtag)'
    print(new_string == 'octothorpe (AKA hashtag)')

    ss = FuzzyString('ss')
    print('\u00df' == ss)

    e = FuzzyString('\u00e9')
    print('\u0065\u0301' == e)
    print('\u0301' in e)


if __name__ == '__main__':
    main()
