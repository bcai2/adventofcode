def part1():
    ans = 0

    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])            

    obstacles = set()
    loc = [0,0]
    cur_dir = 2 # dir starts going up
    dirs = [[1,0],[0,-1],[-1,0],[0,1]]

    for i in range(m):
        for j in range(n):
            c = grid[i][j]
            if c == '.':
                continue
            elif c == '#':
                obstacles.add((i,j))
            else:
                loc = [i,j]

    visited = set()
    while 0 <= loc[0] < m and 0 <= loc[1] < n:
        dx,dy = dirs[cur_dir]
        nx,ny = loc[0] + dx, loc[1] + dy
        if not (0 <= nx < m and 0 <= ny < n):
            visited.add(tuple(loc))
            break
        if grid[nx][ny] == '#':
            cur_dir = (cur_dir + 1) % 4
        else:
            visited.add(tuple(loc))
            loc = [nx,ny]

    ans = len(visited)
    print(ans)

def part2():
    ans = 0

    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])            

    obstacles = set()
    loc = [0,0]
    cur_dir = 2 # dir starts going up
    dirs = [[1,0],[0,-1],[-1,0],[0,1]]

    blanks = []
    for i in range(m):
        for j in range(n):
            c = grid[i][j]
            if c == '.':
                blanks.append((i,j))
                continue
            elif c == '#':
                obstacles.add((i,j))
            else:
                loc = [i,j]

    # big speed potential boost: only search the blanks on the initial path. adding obstacles outside of the path won't change the original (exiting) path
    # this would reduce the search from ~16000 to ~5000 blanks

    loc_init = loc.copy()
    rows = set()
    for i,j in blanks:
        # if (i,j) != (9,7):
        #     # print('skipping')
        #     continue        
        if i not in rows:
            rows.add(i)
            print(i)
        obstacles.add((i,j))
        loc = loc_init
        cur_dir = 2 # dir starts going up
        visited = set()
        exited = False
        while 0 <= loc[0] < m and 0 <= loc[1] < n:
            # print(loc, cur_dir)
            dx,dy = dirs[cur_dir]
            nx,ny = loc[0] + dx, loc[1] + dy
            if not (0 <= nx < m and 0 <= ny < n):
                exited = True
                break
            if (nx,ny) in obstacles:
                cur_dir = (cur_dir + 1) % 4
            else:
                data = (tuple(loc), cur_dir)
                if data not in visited:
                    visited.add(data)
                    loc = [nx,ny]
                else:
                    break
        if not exited:
            ans += 1
        # print(data)
        obstacles.remove((i,j))

    print(ans)

# part1()
part2()