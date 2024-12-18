def part1():
    ans = 0
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        grid[i] = [int(x) for x in grid[i]]

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            cur = 0
            pos = [(i,j)]
            while cur < 9:
                next_pos = []
                for pi,pj in pos:
                    for ni,nj in [(pi+1,pj),(pi-1,pj),(pi,pj+1),(pi,pj-1)]:
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == cur+1:
                            next_pos.append((ni,nj))
                
                cur += 1
                pos = list(set(next_pos))
                if len(pos) == 0:
                    break
            
            if cur == 9:
                print(pos)
                ans += len(pos)

    print(ans)

def part2():
    ans = 0
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        grid[i] = [int(x) for x in grid[i]]

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            cur = 0
            pos = {(i,j): 1}
            while cur < 9:
                next_pos = {}
                for pi,pj in pos:
                    for ni,nj in [(pi+1,pj),(pi-1,pj),(pi,pj+1),(pi,pj-1)]:
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == cur+1:
                            if (ni,nj) not in next_pos:
                                next_pos[(ni,nj)] = 0
                            next_pos[(ni,nj)] += pos[(pi,pj)]
                
                cur += 1
                pos = next_pos
                if len(pos) == 0:
                    break
            
            if cur == 9:
                # print(pos)
                for p in pos:
                    ans += pos[p]

    print(ans)

# part1()
part2()