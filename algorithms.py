import utils
from dataset import DataSet


class ID3:
    def __init__(self):
        pass

    def best_division(self, example_set):
        pass

    def train(self, training_set, attributes, target):
        pass

    def predict(self, tree, sample):
        pass


class KNN:
    def __init__(self, k=5):
        self.training_set = None
        self.k = k
        self.target = None

    def train(self, training_set, target):
        self.training_set = training_set
        self.target = target

    def predict(self, sample):
        distances = [(ex[self.target], self.training_set.distance(ex, sample)) for ex in self.training_set]
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
                # Pr(attr_cls|cls) = Pr(attr_cls and cls) / Pr(c)
                probability *= (len(class_division.matches_attribute(attr, attr_cls)) / examples_of_c)

            pr_c = self.distribution[cls] / len(self.training_set)
            probabilities[cls] = probability * pr_c

        return utils.arg_max(probabilities)
