# from utils import utils

def part1():
    ans = 0
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    seen = set()
    for i in range(m):
        for j in range(n):
            if (i,j) not in seen:
                c = grid[i][j]
                fencing = 0
                area = 0
                q = [(i,j)]
                seen.add((i,j))
                while len(q) > 0:
                    pi,pj = q.pop()
                    area += 1
                    for ni,nj in [(pi+1,pj),(pi-1,pj),(pi,pj+1),(pi,pj-1)]:
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == c:
                            if (ni,nj) not in seen:
                                seen.add((ni,nj))
                                q.append((ni,nj))
                        else:
                            fencing += 1
                # print(i,j,c,area,fencing)
                ans += area * fencing

    print(ans)

def part2():
    ans = 0
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    m = len(grid)
    n = len(grid[0])

    seen = set()
    for i in range(m):
        for j in range(n):
            if (i,j) not in seen:
                c = grid[i][j]
                segments = set()
                area = 0
                q = [(i,j)]
                seen.add((i,j))
                while len(q) > 0:
                    pi,pj = q.pop()
                    area += 1
                    for ni,nj in [(pi+1,pj),(pi-1,pj),(pi,pj+1),(pi,pj-1)]:
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == c:
                            if (ni,nj) not in seen:
                                seen.add((ni,nj))
                                q.append((ni,nj))
                        else:
                            segments.add(((pi,pj),(ni,nj)))

                sides = 0
                while len(segments) > 0:
                    (pi,pj),(ni,nj) = segments.pop()
                    dx,dy = nj-pj,ni-pi

                    dpi,dpj,dni,dnj = pi+dx,pj+dy,ni+dx,nj+dy
                    while ((dpi, dpj), (dni, dnj)) in segments:
                        segments.remove(((dpi, dpj), (dni, dnj)))
                        dpi,dpj,dni,dnj = dpi+dx,dpj+dy,dni+dx,dnj+dy
                    dpi,dpj,dni,dnj = pi-dx,pj-dy,ni-dx,nj-dy
                    while ((dpi, dpj), (dni, dnj)) in segments:
                        segments.remove(((dpi, dpj), (dni, dnj)))
                        dpi,dpj,dni,dnj = dpi-dx,dpj-dy,dni-dx,dnj-dy

                    sides += 1

                # print(i,j,c,area,sides)
                ans += area * sides

    print(ans)

# part1()
part2()