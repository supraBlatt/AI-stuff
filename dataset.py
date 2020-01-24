class DataSet:
    def __init__(self):
        self.example_set = []  # example = {attribute : class}
        self.attr = []  # [(attribute, [classes])]
        self.target = None  # (name, [classes])

    def __getitem__(self, item):  # get example_set[i]
        pass

    ''' CREATION SET FUNCTION '''
    def load_from_file(self, file_name):
        pass

    ''' ATTRIBUTE FUNCTIONS '''
    def matches_attribute(self, attr, cls):
        pass

    def divide_by_attribute(self, attr):
        pass

    def class_distribution(self, attr):
        pass

    ''' SET FUNCTIONS '''
    def distance(self, ex1, ex2):
        pass

    ''' GET FUNCTIONS - deep copy'''
    def attributes(self):
        pass

    def classes(self, attr):
        pass

    def examples(self):
        pass
