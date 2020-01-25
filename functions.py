import math


def entropy(distribution):  # distribution = [#class appearances in data, ..]
    overall = sum(distribution)
    if overall == 0:
        return 0
    probability = [value / overall for value in distribution]
    return -1 * sum([pr * math.log(pr) for pr in probability if pr > 0])


def information_gain(distributions):  # distributions = [ [#class appearances in part1 in the division,..],..]
    overall = sum([sum(dist) for dist in distributions])
    subs = [(sum(dist) / overall) * entropy(dist) for dist in distributions]
    overall_distribution = [sum([dist[i] for dist in distributions]) for i in range(len(distributions[0]))]
    return entropy(overall_distribution) - sum(subs)


# a bit redundant to do it here again but I'm lazy
def class_distribution(examples, attribute):
    pass
