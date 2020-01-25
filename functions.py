import math


def entropy(distribution):  # distribution = [#class appearances in data, ..]
    overall = sum(distribution)
    probability = [value / overall for value in distribution]
    return -1 * sum([pr * math.log(pr) for pr in probability])


def information_gain(attribute, division):  # division = [[examples], ..] division of the overall data
    overall = sum([len(ex) for ex in division])
    distributions = [[]]

    return


# a bit redundant to do it here again but I'm lazy
def class_distribution(examples, attribute):
    pass
