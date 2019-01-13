#!/usr/bin/python3.6

import time
import os, sys


def calculate_neighbours(board, x, y):
    res = 0
    neighbours = {(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)}

    for xn, yn in neighbours:
        if 0 <= (x + xn) < len(board[0]) and 0 <= (y + yn) < len(board):
            res += board[y + yn][x + xn]

    return res


def update(board):
    raws_count = len(board)
    columns_count = len(board[0])
    next_gen = [[0 for _ in range(columns_count)] for _ in range(raws_count)]

    for y in range(raws_count):
        for x in range(columns_count):
            neighbours_count = calculate_neighbours(board, x, y)
            if neighbours_count < 2 or neighbours_count > 3:
                next_gen[y][x] = 0
            elif neighbours_count == 3:
                next_gen[y][x] = 1
            else:
                next_gen[y][x] = board[y][x]

    return next_gen


def print_board(board):
    dead = '\033[1;30m*\033[1;m'
    alive = '\033[1;31mO\033[1;m'

    for raw in board:
        for cell in raw:
            if cell == 1:
                print(alive, end=' ')
            else:
                print(dead, end=' ')
        print()


def get_board():
    board = []
    path = sys.argv[0].rsplit('/', 1)[0] + '/'
    with open(path + 'board.txt', 'r') as board_file:
        for line in board_file:
            board.append([int(n) for n in line.split()])
    return board


def main():
    board = get_board()

    while True:
        os.system('clear')
        print_board(board)
        board = update(board)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
