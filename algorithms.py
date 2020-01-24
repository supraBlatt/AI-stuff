class ID3:
    def __init__(self):
        pass

    def best_division(self, example_set):
        pass

    def train(self, training_set, attributes):
        pass

    def predict(self, tree, sample):
        pass


class KNN:
    def __init__(self, k=5):
        self.training_set = None
        self.k = k

    def train(self, training_set):
        self.training_set = training_set
        pass

    def predict(self, sample):
        pass


class NaiveBayes:
    def __init__(self):
        self.training_set = None

    def train(self, training_set):
        self.training_set = training_set
        pass

    def predict(self, sample):
        pass
