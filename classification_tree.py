def print_node(node):
    pass


class ClassificationTree:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.root = None

    def print_tree(self):
        pass

    def train(self, training_set, target):
        attributes = [attr for attr in training_set.attributes().keys() if attr != target]
        self.root = self.algorithm.train(training_set, attributes, target)
        return

    def predict(self, sample):
        return self.algorithm.predict(self.root, sample)


class Node:
    def __init__(self):
        self.cls = None                    # classification
        self.dividing_by_attribute = None  # attribute name to split the node by
        self.kids = {}                     # {cls : Node}
        self.amount = 0

    def children(self):
        return self.kids

    def classification(self):
        return self.cls

    def attribute(self):
        return self.dividing_by_attribute

    def amount_of_examples(self):
        return self.amount
