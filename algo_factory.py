from classification_tree import ClassificationTree
from algorithms import *


def get_algorithm(alg_name):

    if alg_name == "id3":
        return ClassificationTree(ID3())
    elif alg_name == "knn":
        return KNN()
    elif alg_name == "bayes":
        return NaiveBayes()
    else:
        return None
