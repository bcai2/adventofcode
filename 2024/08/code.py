import math

def part1():
    ans = 0

    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    locs = {}
    for i in range(m):
        for j in range(n):
            c = grid[i][j]
            if c != '.':
                if c not in locs:
                    locs[c] = []
                locs[c].append((i,j))

    antinodes = set()
    for c in locs:
        for i in range(len(locs[c])):
            x1,y1 = locs[c][i]
            for j in range(i+1,len(locs[c])):
                x2,y2 = locs[c][j]
                dx,dy = x2-x1,y2-y1
                
                xa1,ya1 = x2+dx,y2+dy
                xa2,ya2 = x1-dx,y1-dy
                for ax,ay in [(xa1, ya1), (xa2, ya2)]:
                    if 0 <= ax < m and 0 <= ay < n:
                        antinodes.add((ax,ay))

    ans = len(antinodes)
    print(ans)

def part2():
    ans = 0

    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    locs = {}
    for i in range(m):
        for j in range(n):
            c = grid[i][j]
            if c != '.':
                if c not in locs:
                    locs[c] = []
                locs[c].append((i,j))

    antinodes = set()
    for c in locs:
        for i in range(len(locs[c])):
            x1,y1 = locs[c][i]
            for j in range(i+1,len(locs[c])):
                x2,y2 = locs[c][j]
                dx,dy = x2-x1,y2-y1
                dgcd = math.gcd(dx,dy)
                dx //= dgcd
                dy //= dgcd
                
                ax,ay = x2,y2
                while 0 <= ax < m and 0 <= ay < n:
                    antinodes.add((ax,ay))
                    ax += dx
                    ay += dy

                ax,ay = x2,y2
                while 0 <= ax < m and 0 <= ay < n:
                    antinodes.add((ax,ay))
                    ax -= dx
                    ay -= dy                

    ans = len(antinodes)
    print(ans)

part1()
part2()

# testing utils (TODO: delete)
def test():
    from ...utils import utils # testing import
    grid, m, n = utils.get_grid()
    print(grid)

test()