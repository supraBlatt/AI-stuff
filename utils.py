import math

# doesn't keep order
def divide_to_n_parts(lst, n):
    return [lst[pos::n] for pos in range(n)]


def hamming_distance(lst1, lst2):
    to_compare = []
    distance = 0
    tmp1 = lst1[:]
    tmp2 = lst2[:]

    # make tmp1 and tmp2 equal lengths
    if len(tmp1) > len(tmp2):
        distance += len(tmp1) - len(tmp2)
        tmp1 = tmp1[:len(tmp2)]

    # won't do anything if they're already equal in length
    distance += len(tmp2) - len(tmp1)
    tmp2 = tmp2[:len(tmp1)]

    # compare the two lists
    for e1, e2 in zip(tmp1, tmp2):
        if e1 != e2:
            distance += 1
    return distance


def most_common(lst):
    distribution = {}  # {element : #of appearances}

    for e in lst:
        if e not in distribution.keys():
            distribution[e] = 0
        distribution[e] += 1

    # return the most common one
    return max(distribution, key=distribution.get)


def arg_max(dictionary):
    if len(dictionary.keys()) == 0:
        raise Exception("Empty Dictionary")
    return max(dictionary, key=dictionary.get)
