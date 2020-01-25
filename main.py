import algo_factory as factory
import tests

import utils
import algorithms as algos
from dataset import DataSet


def main():
    algorithms = [factory.get_algorithm("id3"),
                  factory.get_algorithm("knn"),
                  factory.get_algorithm("bayes")]

    ds = DataSet()
    target = ds.load_from_file("dataset.txt")

    # run the algorithms
    acc = []
    for alg in algorithms:
        accuracy = tests.k_fold_validation(alg, ds, target, 5)
        acc.append(str(accuracy))

    # write the accuracy into the files
    accuracy_string = '\t'.join(acc)
    with open('accuracy.txt', 'w') as acc_file:
        acc_file.write(accuracy_string)


if __name__ == "__main__":
    main()
