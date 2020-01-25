import algo_factory as factory
import tests


import utils
import algorithms as algos
from dataset import DataSet


def main():
    '''
    algorithms = [factory.get_algorithm("id3"),
                  factory.get_algorithm("knn"),
                  factory.get_algorithm("bayes")]
    '''

    ds = DataSet()
    target = ds.load_from_file("dataset.txt")

    print(utils.divide_to_n_parts([1,2,3,4,5,6,7], 6))
    '''
    knn = algos.KNN()
    knn.train(ds, target)
    print(knn.predict(ds[2]))

    for alg in algorithms:
        accuracy = tests.k_fold_validation(alg, ds, 5)
        print("accuracy = ", accuracy)
    '''

if __name__ == "__main__":
    main()
