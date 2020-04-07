import re

class EasyDict(object):
    def __init__(self, *args, normalize=False, **kwargs):
        self.normalize=normalize
        for dictionary in args:
            for key in dictionary:
                setattr(self, self.normal(key) if self.normalize else key, dictionary[key])
        for key in kwargs:
            setattr(self, self.normal(key) if self.normalize else key, kwargs[key])

    def __getitem__(self, key):
        return getattr(self, self.normal(key) if self.normalize else key)

    def __setitem__(self, key, value):
        setattr(self, self.normal(key) if self.normalize else key, value)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get(self, key, default=None):
        return self.__dict__.get(self.normal(key) if self.normalize else key, default)

    @staticmethod
    def normal(key):
        return re.sub(r'\s', '_', key)


def main():
    person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
    print(person.name)
    # 'Trey Hunner'
    print(person['location'])
    # 'San Diego'

    #print('Bonus 1')
    person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
    person.location = "Portland"
    print(person['location'])
    # 'Portland'
    person['location'] = "San Diego"
    print(person.location)
    # 'San Diego'

    print('Bonus 2')
    person = EasyDict(name="Trey Hunner", location="San Diego")
    print(person.location)
    # 'San Diego'
    print(person == EasyDict(name="Trey", location="San Diego"))
    # False
    print(person == EasyDict(name="Trey Hunner", location="San Diego"))
    # True
    print(person.get('profession'))
    print(person.get('profession', 'unknown'))
    # 'unknown'
    print(person.get('name', 'unknown'))
    # 'Trey Hunner'

    print('Bonus 3')
    person = EasyDict(name="Trey Hunner", location="San Diego", normalize=True)
    person['company name'] = "Truthful Technology LLC"
    print(person.company_name)
    # 'Truthful Technology LLC'
    print(person['company name'])
    # 'Truthful Technology LLC'


if __name__ == '__main__':
    main()

