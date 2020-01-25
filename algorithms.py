import utils, functions
from dataset import *
from classification_tree import *


def best_division(data_set, attributes, target):
    information_gains = {}

    for attr in attributes:
        division = data_set.divide_by_attribute(attr).values()
        distributions = [list(DataSet(div, data_set.attributes()).class_distribution(target).values())
                         for div in division if len(div) > 0]
        information_gains[attr] = functions.information_gain(distributions)
    max_attr = utils.arg_max(information_gains)
    return max_attr, data_set.divide_by_attribute(max_attr)


class ID3:
    def __init__(self):
        pass

    def train(self, training_set, attributes, target):
        if not training_set:
            return None

        root = Node()
        dist = training_set.class_distribution(target)
        most_cls = utils.arg_max(dist)

        # check for leaf -- no more attributes to divide by or homogenous
        if len(attributes) == 0 or dist[most_cls] == len(training_set):
            root.cls = most_cls
            return root

        attribute, division = best_division(training_set, attributes, target)
        div = {cls: [e[attribute] for e in ex] for cls, ex in division.items()}
        root.dividing_by_attribute = attribute
        new_attr = attributes[:]
        new_attr.remove(attribute)

        children = {}
        for cls, examples in division.items():
            child = self.train(DataSet(examples, training_set.attributes()), new_attr, target)
            if child:
                child.amount = len(examples)
                children[cls] = child
        root.kids = children
        return root

    def predict(self, tree, sample):
        if not tree:
            return None

        cur_node = tree
        while not cur_node.classification():
            kids = cur_node.children()

            # if you don't have a route to continue on choose the most populated one
            if sample[cur_node.attribute()] not in kids.keys():
                cur_node = kids[utils.arg_max({cls: child.amount_of_examples() for cls, child in kids.items()})]
            else:
                cur_node = kids[sample[cur_node.attribute()]]
        return cur_node.classification()


class KNN:
    def __init__(self, k=5):
        self.training_set = None
        self.k = k
        self.target = None

    def train(self, training_test, target):
        self.training_set = training_set
        self.target = target

    def predict(self, sample):
        distances = [(ex[self.target], distance(ex, sample, self.target)) for ex in self.training_set]
        if len(distances) == 0:
            return None

        distribution = [tup[0] for tup in sorted(distances, key=lambda x: x[1])][:self.k]
        return utils.most_common(distribution)


class NaiveBayes:
    def __init__(self):
        self.training_set = None     # DataSet training set
        self.target = None           # target attribute name
        self.division_by_class = {}  # {class: DataSet(examples that match class from training set)}
        self.distribution = {}       # {class: #of examples that match class}

    def train(self, training_set, target):
        self.training_set = training_set
        self.target = target

        # dividing the set by target
        dividing = self.training_set.divide_by_attribute(target)  # {class: [examples]}
        self.division_by_class = {name: DataSet(examples, training_set.attributes())
                                  for name, examples in dividing.items()}
        self.distribution = {key: len(examples) for key, examples in dividing.items()}

    def predict(self, sample):
        probabilities = {}

        for cls in self.distribution.keys():

            # all those that match cls
            class_division = self.division_by_class[cls]
            examples_of_c = len(class_division)
            if examples_of_c == 0:
                continue

            # calculate P = Pr(x1|cls)*...
            probability = 1
            for attr, attr_cls in sample.items():
                if attr == self.target:
                    continue

                # Pr(attr_cls|cls) = Pr(attr_cls and cls) / Pr(c)
                probability *= (len(class_division.matches_attribute(attr, attr_cls)) / examples_of_c)

            pr_c = self.distribution[cls] / len(self.training_set)
            probabilities[cls] = probability * pr_c

        return utils.arg_max(probabilities)
