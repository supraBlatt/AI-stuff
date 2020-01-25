import utils

class DataSet:
    def __init__(self):
        self.example_set = []  # [example = {attribute : class},..]
        self.attr = {}         # {name: Attribute}
        self.index = 0         # index for iteration

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

    def matches_attribute(self, attr, cls):
        pass

    def divide_by_attribute(self, attr):
        pass

    def class_distribution(self, attr):
        pass

    ''' SET FUNCTIONS '''

    def distance(self, ex1, ex2):
        return utils.hamming_distance(list(ex1.values()), list(ex2.values()))

    ''' GET FUNCTIONS - deep copy'''

    def attributes(self):
        pass

    def classes(self, attr):
        pass

    def examples(self):
        pass

    def __str__(self):
        s = "dataset\n"
        for att in self.attr.values():
            s += str(att) + '\n'
        s += "Target = " + str(self.target) + '\n'

        for ex in self.example_set:
            s += str(ex)
        return s


''' Basic Data Classes To Make Things More Organised '''


class Attribute:
    def __init__(self, name, classes=[]):
        self.n = name
        self.cls = classes

    def name(self):
        return self.n

    def classes(self):
        return self.cls.copy()

'''
class Example:
    def __init__(self, attributes=[], classes=[]):
        self.values = {key: value for key, value in zip(attributes, classes)}

    def __getitem__(self, attribute):
        if attribute not in self.values.keys():
            raise Exception("No Such Class")
        return self.values[attribute]

    def __str__(self):
        s = "example\n"
        for attr, cls in self.values.items():
            s += "\t|" + attr + " = " + cls + '\n'
        return s
'''