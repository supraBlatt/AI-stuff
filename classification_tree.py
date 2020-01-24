def print_node(node):
    pass


class ClassificationTree:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.root = None

    def print_tree(self):
        pass

    def train(self, training_set):
        self.root = self.algorithm.train(training_set)
        pass

    def predict(self, sample):
        return self.algorithm.predict(self.root, sample)


class Node:
    def __init__(self):
        self.cls = None
        self.dividing_by_attribute = None
        self.kids = {}

    def children(self):
        pass

    def classification(self):
        pass

    def attribute(self):
        pass
