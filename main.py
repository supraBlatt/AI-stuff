import algo_factory as factory
import tests

import utils
import algorithms as algos
from dataset import DataSet


def main():
    algorithms = [factory.get_algorithm("bayes")]

    ds = DataSet()
    target = ds.load_from_file("dataset.txt")
    #sample = {'cap_shape': 'a', 'cap_surface': 's', 'cap_color': 'n', 'bruises': 't', 'odor': 'a', 'gill_attachment': 'f', 'gill_spacing': 'c', 'gill_size': 'n', 'gill_color': 'k', 'stalk_shape': 'e', 'stalk_root': 'e', 'stalk_surface_above_ring': 's', 'stalk_surface_below_ring': 's', 'stalk_color_above_ring': 'w', 'stalk_color_below_ring': 'w', 'veil_type': 'p', 'veil_color': 'w', 'ring_number': 'o', 'ring_type': 'p', 'spore_print_color': 'n', 'population': 's', 'habitat': 'u', 'can_eat': 'no'}

    for alg in algorithms:
        accuracy = tests.k_fold_validation(alg, ds, target, 5)
        print("accuracy = ", accuracy)


if __name__ == "__main__":
    main()
