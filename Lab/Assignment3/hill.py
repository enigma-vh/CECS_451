import random
import time

from board import Board
import numpy as np


def convert1D(board, n):
    arr = [0] * n
    for i in range(n):
        for j in range(n):
            if board.map[i][j] == 1:
                arr[i] = j
    return arr


def convertBoard(b: Board, current_state, row_index):
    for i in range(n):
        if i == current_state[row_index] and b.map[row_index][i] != 1:
            b.flip(row_index, i)
        elif i != current_state[row_index] and b.map[row_index][i] != 0:
            b.flip(row_index, i)


def search_row(b: Board, row_index, current_state, current_fitness):
    b.flip(row_index, current_state[row_index])
    fitness_index = -1
    for j in range(len(b.map[0])):
        if j != current_state[row_index]:
            b.flip(row_index, j)
            tmp_fitness = b.get_fitness()
            if tmp_fitness < current_fitness:
                current_state[row_index] = j
                current_fitness = tmp_fitness
                fitness_index = j
            b.flip(row_index, j)

    if fitness_index == -1:
        b.flip(row_index, current_state[row_index])
    else:
        b.flip(row_index, fitness_index)

    return current_fitness


def hill_climbing(b: Board):
    current_state = convert1D(b, n)
    current_fitness = b.get_fitness()
    for i in range(n):
        current_fitness = search_row(b, i, current_state, current_fitness)


def random_restart(b: Board):
    restarts = 0
    while b.get_fitness() != 0:
        b = Board(n)
        restarts += 1
        hill_climbing(b)
    return b, restarts


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
    board = Board(n)
    start = time.time()
    board, res = random_restart(board)
    end = time.time()

    runtime = (end-start)*1000
    formatted_runtime = "{:.2f}".format(runtime)
    print(f"Running time: {formatted_runtime}ms")
    print_map(board)
