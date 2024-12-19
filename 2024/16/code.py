# from utils import utils
import re, heapq

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
    pq = [(0, (sx, sy, 3))] # score, x, y, dir
    while len(pq) > 0:
        score, (x, y, dir) = heapq.heappop(pq)
        if (x,y,dir) in seen:
            continue
        seen[(x,y,dir)] = score
        if ex == x and ey == y:
            ans = score
            break
        # move
        ox,oy = dirs[dir]
        forward_tuple = (x+ox,y+oy,dir)
        turn1_tuple = (x,y,(dir+1)%4)
        turn2_tuple = (x,y,(dir-1)%4)

        moves = [(score+1000, turn1_tuple), (score+1000, turn2_tuple)]
        if grid[x+ox][y+oy] != '#':
            moves.append((score+1, forward_tuple))

        for new_score, move_tuple in moves:            
            if move_tuple not in seen:
                heapq.heappush(pq, (new_score, move_tuple))

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
    e_score = None
    pq = [(0, (sx, sy, 3), (None, None, None))] # score, x, y, dir, px, py, pd
    while len(pq) > 0:
        score, (x, y, dir), (px, py, pd) = heapq.heappop(pq)
        if e_score is not None and score > e_score:
            break
        if (x,y,dir) in seen:
            if score == seen[(x,y,dir)][0]:
                seen[(x,y,dir)][1].append((px,py,pd))
            continue
        seen[(x,y,dir)] = [score, [(px,py,pd)]]
        if ex == x and ey == y:
            e_score = score
            continue
        # move
        ox,oy = dirs[dir]
        forward_tuple = (x+ox,y+oy,dir)
        turn1_tuple = (x,y,(dir+1)%4)
        turn2_tuple = (x,y,(dir-1)%4)
        present_tuple = (x,y,dir)

        moves = [(score+1000, turn1_tuple), (score+1000, turn2_tuple)]
        if grid[x+ox][y+oy] != '#':
            moves.append((score+1, forward_tuple))

        for new_score, move_tuple in moves:
            if move_tuple not in seen:
                heapq.heappush(pq, (new_score, move_tuple, present_tuple))

    on_best_paths = set()
    seen_best_paths = set()
    for d in range(4):
        if (ex,ey,d) in seen:
            q = [(ex,ey,d)]
            while len(q) > 0:
                x,y,d = q.pop()
                seen_best_paths.add((x,y,d))
                on_best_paths.add((x,y))
                if x == sx and y == sy and d == 3:
                    continue
                for px,py,pd in seen[(x,y,d)][1]:
                    if (px,py,pd) not in seen_best_paths:
                        q.append((px,py,pd))
        
    ans = len(on_best_paths)
    print(ans)
    
# part1()
part2()