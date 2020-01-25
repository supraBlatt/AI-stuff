import algo_factory as factory
import tests

import utils
import algorithms as algos
from dataset import DataSet


def main():
    algorithms = [factory.get_algorithm("knn"),
                  factory.get_algorithm("bayes"),
                  factory.get_algorithm("id3")]

    ds = DataSet()
    target = ds.load_from_file("dataset.txt")

    for alg in algorithms:
        accuracy = tests.k_fold_validation(alg, ds, target, 5)
        print("accuracy = ", accuracy)
        print()


if __name__ == "__main__":
    main()
