import math


def divide_to_n_parts(lst, n):
    [1,2,3,4,5,6,7]
    part_size = math.ceil(len(lst) / n)  # 7 / 5 = 1.4 -> 2
    return [lst[pos:pos + part_size] for pos in range(0, len(lst), part_size)]  # lst[6 [0,2,4,6]


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