# from utils import utils
import re
import heapq

def part1():
    ans = 0
    inputs = []
    with open('input.txt', 'r') as f:
        a, b, p = None, None, None
        for line in f:
            data = [int(x) for x in re.split(r'\D+', line) if len(x) > 0]
            if a is None:
                a = data
            elif b is None:
                b = data
            elif p is None:
                p = data
                inputs.append([a,b,p])
            else:
                a, b, p = None, None, None

    print(len(inputs))
    for input in inputs:
        ans += find_cheapest_path_linalg(input)

    print(ans)

def find_cheapest_path(input):
    # print(input)
    (ax, ay), (bx, by), (px, py) = input
    # mx = max(ax, bx)
    # my = max(ay, by)

    pq = [(0, 0, 0, 0, 0)]
    seen = set()
    while len(pq) > 0:
        c, x, y, na, nb = heapq.heappop(pq)
        if (x,y) in seen:
            continue
        seen.add((x,y))
        if x == px and y == py:
            return c
        if x + ax <= px and y + ay <= py and na < 100:
            heapq.heappush(pq, (c+3, x+ax, y+ay, na+1, nb))
        if x + bx <= px and y + by <= py and nb < 100:
            heapq.heappush(pq, (c+1, x+bx, y+by, na, nb+1))

    return 0

def find_cheapest_path_linalg(input):
    (ax, ay), (bx, by), (px, py) = input
    det = ax * by - bx * ay
    if det == 0:
        print('multiples!') # THIS NEVER HAPPENS, WE CAN DISREGARD
        cost = 0
        ma = px // ax
        if ax * ma == px and ay * ma == py:
            cost = ma * 3
        mb = px // bx
        if bx * mb == px and by * mb == py:
            cost = mb if cost == 0 else min(cost, mb)
        # this is faulty. in an ideal world, we'd try to find the cost minimizing function between # of A presses and # of B presses. but we don't have to worry about that here
        return cost
    
    na_times_det, nb_times_det = by * px - bx * py, -ay * px + ax * py
    if na_times_det % abs(det) != 0 or nb_times_det % abs(det) != 0:
        return 0
    na, nb = na_times_det // det, nb_times_det // det
    return 3 * na + nb


def part2():
    ans = 0
    inputs = []
    with open('input.txt', 'r') as f:
        a, b, p = None, None, None
        for line in f:
            data = [int(x) for x in re.split(r'\D+', line) if len(x) > 0]
            if a is None:
                a = data
            elif b is None:
                b = data
            elif p is None:
                p = [x + 10000000000000 for x in data]
                inputs.append([a,b,p])
            else:
                a, b, p = None, None, None

    print(len(inputs))
    for input in inputs:
        ans += find_cheapest_path_linalg(input)

    print(ans)

part1()
part2()