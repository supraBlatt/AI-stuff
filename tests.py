import utils
from dataset import DataSet


def accuracy(classifier_answers, true_answers):
    # acc = (correct / overall) = ((overall - incorrect)/ overall) = 1 - (incorrect/overall)
    incorrect = utils.hamming_distance(classifier_answers, true_answers)
    return 1 - (incorrect / len(true_answers))


def k_fold_validation(algorithm, training_set, target_attribute, k):
    examples = [ex for ex in training_set]
    parts = [lst for lst in utils.divide_to_n_parts(examples, k) if len(lst) > 0]

    overall_accuracy = 0

    # take 1 and leave all the rest as training sets
    for i in range(len(parts)):
        example_set = parts[:i] + parts[i+1:]
        example_set = [j for i in example_set for j in i]

        training_set = DataSet(example_set, training_set.attributes())
        validation_set = parts[i]

        acc = validate(algorithm, training_set, validation_set, target_attribute)
        print("Accuracy: ", acc)
        overall_accuracy += acc

    return overall_accuracy / len(parts)


def validate(algorithm, training_set, validation_set, target_attribute):
    # for accuracy calculations
    classifier_answers = []
    true_answers = []
    # train and predict
    algorithm.train(training_set, target_attribute)
    count = 0
    for sample in validation_set:
        classifier_answers.append(algorithm.predict(sample))
        true_answers.append(sample[target_attribute])
        count += 1

    return accuracy(classifier_answers, true_answers)
