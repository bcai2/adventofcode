# from utils import utils
import re, heapq

def part1():
    ans = 0
    coords = []
    with open('input.txt', 'r') as f:
        for line in f:
            data = [int(x) for x in re.split(r'[^\-\d]+', line) if len(x) > 0]
            coords.append(data)
    
    dim = 71
    corrupted = {tuple(c):i for i,c in enumerate(coords[:1024])}
    seen = {}
    pq = [(0,(0,0))]
    while len(pq) > 0:
        d,(x,y) = heapq.heappop(pq)
        if (x,y) in seen:
            continue
        seen[(x,y)] = d
        if x == dim-1 and y == dim-1:
            ans = d
            break
        offsets = [(0,1),(1,0),(0,-1),(-1,0)]
        for ox,oy in offsets:
            dx, dy = x+ox, y+oy
            if 0 <= dx < dim and 0 <= dy < dim and (dx,dy) not in corrupted:
                heapq.heappush(pq, (d+1, (dx,dy)))

    for i in range(dim):
        row = []
        for j in range(dim):
            if (i,j) in corrupted:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))
    # print(corrupted)
    # print([c for c in seen])
    print(ans)

def part2():
    ans = 0
    coords = []
    with open('input.txt', 'r') as f:
        for line in f:
            data = [int(x) for x in re.split(r'[^\-\d]+', line) if len(x) > 0]
            coords.append(data)
    dim = 71

    corrupted = {tuple(c):i for i,c in enumerate(coords)}
    unreachable_time = 0
    for t in range(2800,len(coords)):
        if t % 100 == 0:
            print(t)
        path_exists = False
        seen = {}
        pq = [(0,(0,0))]
        while len(pq) > 0:
            d,(x,y) = heapq.heappop(pq)
            if (x,y) in seen:
                continue
            seen[(x,y)] = d
            if x == dim-1 and y == dim-1:
                path_exists = True
                break
            offsets = [(0,1),(1,0),(0,-1),(-1,0)]
            for ox,oy in offsets:
                dx, dy = x+ox, y+oy
                if 0 <= dx < dim and 0 <= dy < dim and ((dx,dy) not in corrupted or corrupted[(dx,dy)] >= t):
                    heapq.heappush(pq, (d+1, (dx,dy)))
        if not path_exists:
            unreachable_time = t-1
            break
        
    ans = coords[unreachable_time]
    print(unreachable_time)
    print(ans)

part1()
part2()