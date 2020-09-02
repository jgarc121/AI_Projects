# !/usr/bin/env python3
# Beyond Search Homework
# By: Jose Garcia
import sys
import random

solved1 = 0
solved2 = 0
solved3 = 0
cost1 = 0
cost2 = 0
cost3 = 0


def generate_random_board():
    random_board = [random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8),
                    random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)]
    return random_board


def check_heuristic(board):
    heuristic = 0
    for index1 in range(len(board)):
        descending_Calc1 = index1 + board[index1]
        n = 1
        for index2 in range(index1 + 1, len(board)):

            descending_Calc2 = index2 + board[index2]

            if (board[index1] == board[index2]) or (descending_Calc1 == descending_Calc2) or (
                    ((index1 + n) == index2) and ((board[index1] + n) == board[index2])):
                heuristic += 1
            n += 1

    return heuristic


def steepest_ascent_HC(board):
    global cost1
    current_heuristic = check_heuristic(board)
    if current_heuristic == 0:
        return current_heuristic
    else:
        for i in range(len(board)):
            j = 1
            original = board[i]
            while j <= len(board):
                cost1 += 1
                board[i] = j
                if check_heuristic(board) < current_heuristic:
                    return steepest_ascent_HC(board)
                j += 1
            board[i] = original
    return current_heuristic


def random_HC(board):
    global cost3
    current_heuristic = check_heuristic(board)
    if current_heuristic == 0:
        return True
    else:
        for i in range(len(board)):
            j = 1
            original = board[i]
            while j <= len(board):
                cost3 += 1
                board[i] = j
                if check_heuristic(board) < current_heuristic:
                    return random_HC(board)
                j += 1
            board[i] = original
    return random_HC(generate_random_board())



if __name__ == "__main__":
    count = sys.argv[1]

    done = False
    i = 0
    while i < int(count):
        done = False
        random_board = generate_random_board()
        while not done:
            if steepest_ascent_HC(random_board) == 0:
                solved1 += 1
            if genetic_algorithm(generate_random_board(), generate_random_board(), generate_random_board(),
                                 generate_random_board()):
                solved2 += 1
            if random_HC(random_board):
                solved3 += 1
            done = True
        i += 1
    print(str(count) + ' puzzles.')
    print('Steepest-HillClimbing: ' + str((solved1 / int(count)) * 100) + '% solved, average search cost: ' + str(
        cost1) + ';')
    print('Genetic Algorithm: ' + str((solved2 / int(count)) * 100) + '% solved, average search cost: ' + str(
        cost2) + ';')
    print(
        'Random-Restart Hill-Climbing:  ' + str((solved3 / int(count)) * 100) + '% solved, average search cost: ' + str(
            cost3) + ';')

