import random


def sampling_probability():
    pC_R = [0.878, 0.122]
    pC_negR = [0.3103, 0.6897]
    pR_C = [0.9863, 0.0137]
    pR_negC = [0.8182, 0.1818]

    print("\nPart A. The sampling probabilities")
    print("P(C|-s,r) = <{a:.4f}, {b:.4f}>".format(a=pC_R[0], b=pC_R[1]))
    print("P(C|-s,-r) = <{a:.4f}, {b:.4f}>".format(a=pC_negR[0], b=pC_negR[1]))
    print("P(R|c,-s,w) = <{a:.4f}, {b:.4f}>".format(a=pR_C[0], b=pR_C[1]))
    print("P(R|-c,-s,w) = <{a:.4f}, {b:.4f}>".format(a=pR_negC[0], b=pR_negC[1]))


def transition_matrix():
    transitionMatrix = [[0.9322, 0.0068, 0.0610, 0.0000],
                        [0.4932, 0.162, 0.0000, 0.3448],
                        [0.4390, 0.0000, 0.4701, 0.0909],
                        [0.0000, 0.1552, 0.4091, 0.4357]]

    states = ["  ", "S1", "S2", "S3", "S4"]

    print("\nPart B. The transition probability matrix")
    for i in states:
        print(i, end="\t\t  ")
    print()

    for i in range(len(transitionMatrix)):
        print("S{a}".format(a=i + 1), end="\t\t")
        for j in range(len(transitionMatrix[0])):
            print("{:.4f}".format(transitionMatrix[i][j]), end="\t\t")
        print()


def mcmc():
    curr_state = "S1"
    next_state = ""
    runs = [curr_state]
    S1_count = 0
    S2_count = 0
    S3_count = 0
    S4_count = 0

    for i in range(1, 10 ** 6):
        rand = random.random()
        if curr_state == "S1":
            if rand > 0.0610:
                next_state = "S1"
            elif rand > 0.0068:
                next_state = "S3"
            else:
                next_state = "S2"
        elif curr_state == "S2":
            if rand > 0.3448:
                next_state = "S1"
            elif rand > 0.162:
                next_state = "S4"
            else:
                next_state = "S2"
        elif curr_state == "S3":
            if rand > 0.4390:
                next_state = "S3"
            elif rand > 0.0909:
                next_state = "S1"
            else:
                next_state = "S4"
        else:
            if rand > 0.4091:
                next_state = "S4"
            elif rand > 0.1552:
                next_state = "S3"
            else:
                next_state = "S1"
        curr_state = next_state
        runs.append(curr_state)

    for st in runs:
        if st == "S1":
            S1_count += 1
        elif st == "S2":
            S2_count += 1
        elif st == "S3":
            S3_count += 1
        else:
            S4_count += 1

    # print(S1_count, S2_count, S3_count, S4_count)
    posC = (S1_count + S2_count) / (10 ** 6)
    negC = (S3_count + S4_count) / (10 ** 6)
    print("\nPart C. The probability for the query")
    print("P(C|-s,w) = <{a:.4f}, {b:.4f}>".format(a=posC, b=negC))


if __name__ == '__main__':
    sampling_probability()
    transition_matrix()
    mcmc()  # bayes' result = [0.85658, 0.14342]
