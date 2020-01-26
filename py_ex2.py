import algo_factory as factory
import tests
from dataset import DataSet


def main():
    algorithms = [factory.get_algorithm("id3"),
                  factory.get_algorithm("knn"),
                  factory.get_algorithm("bayes")]

    training = DataSet()
    print("gay" + training[0])
    target = training.load_from_file("train.txt")

    validation = DataSet()
    validation.load_from_file("test.txt")

    output_file = "output.txt"
    another_one = DataSet()
    print("k = ", len(another_one))

    # run the algorithms
    acc = []
    for i in range(len(algorithms)):
        print("Starting alg ", i)
        accuracy = tests.validate(algorithms[i], training, validation, target)
        print("accuracy = ", accuracy)
        # print specifically the tree algorithm
        if i == 0:
            algorithms[i].print_tree(output_file)
        acc.append(str(accuracy))

    # write the accuracy into the files
    accuracy_string = '\n' + '\t'.join(acc)
    print("Overall accuracy string =", accuracy_string)
    with open(output_file, 'a') as acc_file:
        acc_file.write(accuracy_string)


if __name__ == "__main__":
    main()
