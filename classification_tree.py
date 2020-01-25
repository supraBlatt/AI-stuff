def print_in_depth(cur_node, depth):
    start = '\t'*depth
    if depth > 0:
        start += '|'
    printed = ""
    for cls, child in cur_node.children().items():
        printed += start + cur_node.attribute() + "=" + cls

        if child.classification():
            printed += ":" + child.classification() + '\n'
        else:
            printed += '\n' + print_in_depth(child, depth + 1)
    return printed


class ClassificationTree:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.root = None

    def print_tree(self):
        with open('tree.txt', 'w') as output:
            output.write(print_in_depth(self.root, 0))

    def train(self, training_set, target):
        attributes = [attr for attr in training_set.attributes().keys() if attr != target]
        self.root = self.algorithm.train(training_set, attributes, target)
        self.print_tree()
        return

    def predict(self, sample):
        return self.algorithm.predict(self.root, sample)


class Node:
    def __init__(self):
        self.cls = None                    # classification
        self.dividing_by_attribute = ""  # attribute name to split the node by
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
