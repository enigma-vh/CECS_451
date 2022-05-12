import random
import time
from board import Board
import numpy as np


def random_selection(states, probabilities):
    return np.random.choice(states, numsState, p=probabilities)


def get_probability(fitness):
    prob = np.asarray(fitness).astype("float64")
    return prob / sum(prob)


def convert1D(board, n):
    arr = [0] * n
    for i in range(n):
        for j in range(n):
            if board.map[i][j] == 1:
                arr[i] = j
    return arr


def cross_over(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n], y[0:c] + x[c:n]


def mutation(x):
    n = len(x)
    pos = random.randint(-1, n - 1)
    m = random.randint(0, n - 1)
    if pos != -1:
        x[pos] = m


def modify_board(b: Board, oBoard, mBoard):
    for i in range(len(oBoard)):
        b.flip(i, oBoard[i])
        b.flip(i, mBoard[i])


def genetic_alogrithm(p, f, encoded):
    probabilities = get_probability(f)
    new_encoded = []
    sel = random_selection(list(range(0, numsState)), probabilities)

    for j in range(0, len(sel), 2):
        x, y = cross_over(encoded[sel[j]], encoded[sel[j + 1]])
        mutation(x)
        mutation(y)
        modify_board(p[j], encoded[j], x)
        modify_board(p[j + 1], encoded[j + 1], y)
        new_encoded.append(x)
        new_encoded.append(y)
        if p[j].get_fitness() == 0 or p[j + 1].get_fitness() == 0:
            break

    return new_encoded


def print_map(b:  Board):
    for i in range(n):
        for j in range(n):
            if b.map[i][j] == 0:
                print("-", end=' ')
            else:
                print(b.map[i][j], end=' ')
        print()


if __name__ == '__main__':
    n = 5
    numsState = 8
    maxFitness = n * (n - 1) / 2
    population = [Board(n) for _ in range(numsState)]
    e = [convert1D(board, n) for board in population]

    start = time.time()
    while maxFitness not in [(maxFitness - board.get_fitness()) for board in population]:
        fitness = [maxFitness - board.get_fitness() for board in population]
        tmp = genetic_alogrithm(population, fitness, e)
        e = tmp
    end = time.time()

    runtime = (end-start)*1000
    formatted_runtime = "{:.2f}".format(runtime)
    for state in population:
        if state.get_fitness() == 0:
            print(f"Running time: {formatted_runtime}ms")
            print_map(state)
            break
