import re, os

def get_grid():
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    return grid, m, n

def get_digits():
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            data = [int(x) for x in re.split(r'[^\-\d]+', line) if len(x) > 0] # gets digits and hyphens
            lines.append(data)
    return lines