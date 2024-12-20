# from utils import utils
import re, heapq, bisect

def part1():
    ans = 0
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    sx,sy,ex,ey = [None]*4
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                sx,sy=i,j
            elif grid[i][j] == 'E':
                ex,ey=i,j

    dirs = [[1,0],[0,-1],[-1,0],[0,1]]
    seen = {}
    pq = [(0, (ex, ey))]
    while len(pq) > 0:
        t, (x, y) = heapq.heappop(pq)
        if (x,y) in seen:
            continue
        seen[(x,y)] = t
        # move
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if grid[nx][ny] != '#' and (nx,ny) not in seen:
                heapq.heappush(pq, (t+1, (nx, ny)))

    pq = [(0, (sx, sy))]
    two_steps = [[2,0],[1,1],[0,2],[-1,1],[-2,0],[-1,-1],[0,-2],[1,-1]]
    path_seen = {}
    while len(pq) > 0:
        t, (x, y) = heapq.heappop(pq)
        if (x,y) in path_seen:
            continue
        path_seen[(x,y)] = t

        if x == ex and y == ey:
            break

        # cheat
        for tx,ty in two_steps:
            ntx, nty = x+tx, y+ty
            if (ntx,nty) not in seen:
                continue
            total_time = seen[(x+tx,y+ty)]+t+2
            if seen[(sx,sy)] - total_time >= 100:
                ans += 1

        # move
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if grid[nx][ny] != '#' and (nx,ny) not in path_seen:
                heapq.heappush(pq, (t+1, (nx, ny)))

    # print(len(path_seen))
    print(ans)

def part2():
    ans = 0
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    sx,sy,ex,ey = [None]*4
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                sx,sy=i,j
            elif grid[i][j] == 'E':
                ex,ey=i,j

    dirs = [[1,0],[0,-1],[-1,0],[0,1]]
    seen = {}
    pq = [(0, (ex, ey))]
    while len(pq) > 0:
        t, (x, y) = heapq.heappop(pq)
        if (x,y) in seen:
            continue
        seen[(x,y)] = t
        # move
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if grid[nx][ny] != '#' and (nx,ny) not in seen:
                heapq.heappush(pq, (t+1, (nx, ny)))

    seen_steps = set([(0,0)])
    layers = [[(0,0)]]
    for i in range(20):
        next_layer = []
        for lx,ly in layers[-1]:
            for dx,dy in dirs:
                nx,ny = lx+dx,ly+dy
                if (nx,ny) not in seen_steps:
                    seen_steps.add((nx,ny))
                    next_layer.append((nx,ny))
        layers.append(next_layer)

    print(sum(len(x) for x in layers))

    # print(len([seen[c] for c in seen if seen[c] <= seen[(sx,sy)]])) # path is linear!
    sorted_coords = sorted([(seen[c], c) for c in seen if seen[c] <= seen[(sx,sy)]])
    # print(seen[(sx,sy)])
    for t,c in sorted_coords:
        if t % 500 == 0:
            print(t)
        # if t < 100:
        #     continue
        cx, cy = c
        # if t < 941:
        #     for lt,lc in sorted_coords[:t-100]:
        #         lcx, lcy = lc
        #         if t - (lt + abs(lcx-cx) + abs(lcy-cy)) >= 100:
        #             ans += 1
        # else:
        #     for d in range(1,21):
        #         for dx,dy in layers[d]:
        #             lcx, lcy = cx+dx, cy+dy
        #             if (lcx,lcy) in seen and t - (seen[(lcx,lcy)] + abs(lcx-cx) + abs(lcy-cy)) >= 100:
        #                 ans += 1
        
        for d in range(1,21):
            for dx,dy in layers[d]:
                lcx, lcy = cx+dx, cy+dy
                if (lcx,lcy) in seen and t - (seen[(lcx,lcy)] + d) >= 100:
                    ans += 1

    # print(len(path_seen))
    print(ans)

# part1()
part2()