class PermaDict(dict):
    def __setitem__(self, key, value):
        if key in self.keys():
            raise KeyError(f"'{key}' already in dictionary.")
        else:
            super().__setitem__(key, value)


def main():
    locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
    print(list(locations))
    print(list(locations.values()))
    print(list(locations.items()))

    locations = PermaDict({'David': "Boston"})
    locations['David'] = "Amsterdam"
    locations['Andrii'] = "Kyiv"

    print(locations)


if __name__ == '__main__':
    main()