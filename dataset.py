import utils


def distance(ex1, ex2, target):
    new_ex1 = {key: value for key, value in ex1.items() if key != target}
    new_ex2 = {key: value for key, value in ex2.items() if key != target}
    return utils.hamming_distance(list(new_ex1.values()), list(new_ex2.values()))


class DataSet:
    def __init__(self, example_set=[], attributes={}):
        self.example_set = example_set  # [example = {attribute : class},..]
        self.attr = attributes          # {name: Attribute}
        self.index = 0                  # index for iteration

    ''' ITERATION FUNCTIONS'''

    def __getitem__(self, item):  # get example_set[i]
        if item >= len(self.example_set):
            raise IndexError('Example Index Out Of Range')

        return self.example_set[item].copy()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            result = self[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return result

    def __len__(self):
        return len(self.example_set)

    ''' CREATION SET FUNCTION '''

    # returns the target attribute
    def load_from_file(self, file_name):
        with open(file_name, 'r') as database:

            # assuming attributes are at the first line
            attributes = database.readline()
            if not attributes:
                raise Exception('Empty File')

            attributes = attributes.strip().split('\t')
            classes = {key: [] for key in attributes}

            # go over all examples
            for line in database:
                class_line = line.strip().split('\t')

                # fill in our known classes
                for attr, cls in zip(attributes, class_line):
                    classes[attr].append(cls)

                # create the example
                example = {key: value for key, value in zip(attributes, class_line)}
                self.example_set.append(example)

            # fill in the attributes - assuming the target is the last attribute
            self.attr = {name: Attribute(name, cls) for name, cls in classes.items()}
            target = attributes[-1]
            return target

    ''' ATTRIBUTE FUNCTIONS '''

    def matches_attribute(self, attribute, cls):
        if attribute not in self.attr.keys():
            raise Exception("Not A Valid Attribute")
        if cls not in self.attr[attribute].classes():
            raise Exception("Not A Valid Class")

        matches = []
        for ex in self.example_set:
            if ex[attribute] == cls:
                matches.append(ex)
        return matches

    def divide_by_attribute(self, attribute):
        if attribute not in self.attr.keys():
            raise Exception("Not A Valid Attribute")
        classes = self.attr[attribute].classes()

        division = {}
        for cls in classes:
            division[cls] = []

        for example in self.example_set:
            division[example[attribute]].append(example)

        return division

    def class_distribution(self, attribute):
        division = self.divide_by_attribute(attribute)
        return {key: len(value) for key, value in division.items()}

    ''' GET FUNCTIONS - deep copy'''

    def attributes(self):
        return {attr.name(): Attribute(attr.name(), attr.classes()) for attr in self.attr.values()}



''' Basic Data Classes To Make Things More Organised '''


class Attribute:
    def __init__(self, name, classes=[]):
        self.n = name
        self.cls = classes

    def name(self):
        return self.n

    def classes(self):
        return self.cls.copy()
