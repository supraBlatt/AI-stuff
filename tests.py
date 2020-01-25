import utils


def accuracy(classifier_answers, true_answers):

    # acc = (correct / overall) = ((overall - incorrect)/ overall) = 1 - (incorrect/overall)
    incorrect = utils.hamming_distance(classifier_answers, true_answers)
    return 1 - (incorrect / len(true_answers))


def k_fold_validation(algorithm, training_set, k):
    pass
