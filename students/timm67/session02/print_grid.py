#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
Print Grid Exercise
"""

_star = '*'
_line = '-'
_intersect = '+'
_vertline = '|'
_space = ' '


def print_grid(n):
    global _star, _line, _intersect, _vertline, _space
    outlines = []
    cur_row = 0
    cur_col = 0

    if n < 11:
        n = n * 2 + 1

    for j in range(n):
        grid = ''
        cur_col = 0
        for i in range(n):
            if (cur_row % (n // 2)) == 0 and (cur_col % (n // 2)) == 0:
                grid += _intersect
            elif (cur_row % (n // 2)) == 0:
                grid += _line
            elif (cur_col % (n // 2) == 0):
                grid += _vertline
            else:
                grid += _space
            cur_col += 1
        cur_row += 1
        outlines.append(grid)

    for line in outlines:
        print(line)


def print_grid2(num_columns, column_width):
    global _star, _line, _intersect, _vertline, _space
    outlines = []
    cur_row = 0
    cur_col = 0

    for j in range(num_columns*column_width+1):
        grid = ''
        cur_col = 0
        for i in range(num_columns*column_width+1):
            if (cur_row % column_width) == 0 and (cur_col % column_width) == 0:
                grid += _intersect
            elif (cur_row % column_width) == 0:
                grid += _line
            elif (cur_col % column_width) == 0:
                grid += _vertline
            else:
                grid += _space
            cur_col += 1
        cur_row += 1
        outlines.append(grid)

    for line in outlines:
        print(line)

if __name__ == "__main__":
    print('\n\nprint_grid(15)\n\n')
    print_grid(15)
    print('\n\nprint_grid(13)\n\n')
    print_grid(11)
    print('\n\nprint_grid(3)\n\n')
    print_grid(3)
    print('\n\nprint_grid2(3, 4)\n\n')
    print_grid2(3, 4)
    print('\n\nprint_grid2(5, 3)\n\n')
    print_grid2(5, 3)
