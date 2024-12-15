def part1():
    ans = 0

    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    
    dirs = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            for dx,dy in dirs:
                if i+3*dx >= m or i+3*dx < 0 or j+3*dy >= n or j+3*dy < 0:
                    continue
                seq = [[i,j],[i+dx,j+dy],[i+2*dx,j+2*dy],[i+3*dx,j+3*dy]]
                traced = ''.join(grid[tx][ty] for tx,ty in seq)
                if traced == 'XMAS':
                    ans += 1

    print(ans)

def part2():
    ans = 0
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())


    m = len(grid)
    n = len(grid[0])
    for i in range(1,m-1):
        for j in range(1,n-1):
            if grid[i][j] == 'A':
                # across_pair = ''.join(sorted([grid[i-1][j], grid[i+1][j]]))
                # down_pair = ''.join(sorted([grid[i][j+1], grid[i][j-1]]))
                # if across_pair == 'MS' and down_pair == 'MS':
                #     ans += 1

                diag1_pair = ''.join(sorted([grid[i-1][j+1], grid[i+1][j-1]]))
                diag2_pair = ''.join(sorted([grid[i-1][j-1], grid[i+1][j+1]]))
                if diag1_pair == 'MS' and diag2_pair == 'MS':
                    ans += 1

    print(ans)

# part1()
part2()