# from utils import utils
import re, heapq

def part1():
    ans = 0
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            data = [int(x) for x in re.split(r'[^\d\-]+', line) if len(x) > 0] # gets digits and hyphens
            lines.append(data)
    # print(lines)
    
    quad_counts = [0]*4
    epochs = 100
    lx = 101
    # lx = 11
    ly = 103
    # ly = 7

    mx = lx // 2
    my = ly // 2
    for data in lines:
        px,py,vx,vy = data
        pfx, pfy = (px + epochs * vx) % lx, (py + epochs * vy) % ly
        # print(pfx, pfy)

        if pfx < mx:
            if pfy < my:
                quad_counts[0] += 1
            elif pfy > my:
                quad_counts[1] += 1
        elif pfx > mx:
            if pfy < my:
                quad_counts[2] += 1
            elif pfy > my:
                quad_counts[3] += 1

    # print(quad_counts)
    ans = 1
    for c in quad_counts:
        ans *= c
    print(ans)

def part2():
    ans = 0
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            data = [int(x) for x in re.split(r'[^\d\-]+', line) if len(x) > 0] # gets digits and hyphens
            lines.append(data)

    lx = 101
    ly = 103
    epochs = lx * ly

    # weird horizontal arrangement at 87 mod 103 times
    # weird vertical arrangement at 33 mod 101 times

    line_guess = ['.']*50 + ['O'] + ['.']*50
    with open('output.txt', 'w') as f:
        for t in range(7709,7709+1):
            if t % 500 == 0:
                print(t)
            f.write(f'{t}\n')
            points = set()
            for data in lines:
                px,py,vx,vy = data
                pfx, pfy = (px + t * vx) % lx, (py + t * vy) % ly
                points.add((pfx, pfy))
            
            # has_line_guess = False
            rows = []
            for j in range(ly):
                row = []
                for i in range(lx):
                    if (i,j) in points:
                        row.append('O')
                    else:
                        row.append('.')
                # if row == line_guess:
                    # has_line_guess = True
                full_row = ''.join(row)
                rows.append(full_row)
            for r in rows:
                f.write(f'{r}\n')

    # print(ans)

# part1()
part2()