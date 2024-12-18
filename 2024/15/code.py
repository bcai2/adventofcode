# from utils import utils
import re, heapq

def part1():
    ans = 0
    grid = []
    moves = []
    with open('input.txt', 'r') as f:
        grid_filled = False
        for line in f:
            if len(line.strip()) == 0:
                grid_filled = True
            elif not grid_filled:
                grid.append([x for x in line.strip()])
            else:
                moves.append(line.strip())
    moves = ''.join(moves)

    m = len(grid)
    n = len(grid[0])

    loc = None
    for i in range(m):
        if loc is not None:
            break
        for j in range(n):
            if grid[i][j] == '@':
                loc = [i,j]
                break

    offset = {'^':[-1,0],'>':[0,1],'v':[1,0],'<':[0,-1]}
    for move in moves:
        ox,oy = offset[move]
        sx,sy = loc
        nx,ny = sx+ox,sy+oy
        box_pushed = False
        while 0 <= nx < m and 0 <= ny < n:
            if grid[nx][ny] == '#':
                break
            elif grid[nx][ny] == '.':
                if not box_pushed:
                    grid[nx][ny] = '@'
                    loc = [nx,ny]
                else:
                    grid[nx][ny] = 'O'
                    grid[sx+ox][sy+oy] = '@'
                    loc = [sx+ox,sy+oy]
                grid[sx][sy] = '.'
                break
            else: # box ('O') encountered
                box_pushed = True
                nx += ox
                ny += oy
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                ans += 100 * i + j

    print(ans)

def part2():
    ans = 0
    grid = []
    moves = []
    with open('input.txt', 'r') as f:
        grid_filled = False
        for line in f:
            if len(line.strip()) == 0:
                grid_filled = True
            elif not grid_filled:
                grid.append([x for x in line.strip()])
            else:
                moves.append(line.strip())
    moves = ''.join(moves)

    big_grid = []
    for r in grid:
        new_r = []
        for c in r:
            if c == '#':
                new_r.append('#')
                new_r.append('#')
            elif c == 'O':
                new_r.append('[')
                new_r.append(']')
            elif c == '.':
                new_r.append('.')
                new_r.append('.')
            elif c == '@':
                new_r.append('@')
                new_r.append('.')
        big_grid.append(new_r)
    grid = big_grid

    m = len(grid)
    n = len(grid[0])

    loc = None
    for i in range(m):
        if loc is not None:
            break
        for j in range(n):
            if grid[i][j] == '@':
                loc = [i,j]
                break

    offset = {'^':[-1,0],'>':[0,1],'v':[1,0],'<':[0,-1]}
    for move in moves:
        # print(move)
        ox,oy = offset[move]
        sx,sy = loc
        layers = [[[sx,sy]]]
        valid_push = True
        while len(layers[-1]) > 0 and valid_push:
            next_layer = set()
            for px,py in layers[-1]:
                nx,ny = px+ox,py+oy
                if grid[nx][ny] == '#':
                    valid_push = False                    
                    break
                elif grid[nx][ny] == '[':
                    next_layer.add((nx,ny))
                    if ox != 0:
                        next_layer.add((nx,ny+1))
                elif grid[nx][ny] == ']':
                    next_layer.add((nx,ny))
                    if ox != 0:
                        next_layer.add((nx,ny-1))
            layers.append(list(next_layer))
            
        if valid_push:
            while len(layers) > 0:
                outer_layer = layers.pop()
                for px,py in outer_layer:
                    nx,ny = px+ox,py+oy
                    grid[nx][ny] = grid[px][py]
                    grid[px][py] = '.'
            loc = [sx+ox, sy+oy]
    
    # for r in grid:
    #     print(''.join(r))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '[':
                ans += 100 * i + j

    print(ans)

# part1()
part2()