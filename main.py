import algo_factory as factory
import tests
from dataset import DataSet


def main():
    algorithms = [factory.get_algorithm("id3"),
                  factory.get_algorithm("knn"),
                  factory.get_algorithm("bayes")]

    ds = DataSet()
    ds.load_from_file("dataset.txt")

    for alg in algorithms:
        accuracy = tests.k_fold_validation(alg, ds, 5)
        print("accuracy = ", accuracy)


if __name__ == "__main__":
    main()
