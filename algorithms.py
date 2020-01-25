import utils

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
        distribution = [tup[0] for tup in sorted(distances, key=lambda x: x[1])][:self.k]
        return utils.most_common(distribution)


class NaiveBayes:
    def __init__(self):
        self.training_set = None
        self.target = None

    def train(self, training_set, target):
        self.training_set = training_set
        self.target = target

    def predict(self, sample):
        pass
