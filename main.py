import algo_factory as factory
import tests

import utils
import algorithms as algos
from dataset import DataSet


def main():
    algorithms = [factory.get_algorithm("bayes")]

    ds = DataSet()
    target = ds.load_from_file("dataset.txt")
    print(str(ds[0]))
    for alg in algorithms:
        alg.train(ds, target)
        print(alg.predict(sample))

    '''
    for alg in algorithms:
        accuracy = tests.k_fold_validation(alg, ds, target, 5)
        print("accuracy = ", accuracy)
    '''

if __name__ == "__main__":
    main()
