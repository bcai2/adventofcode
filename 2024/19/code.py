# from utils import utils
import re, heapq, bisect

def part1():
    ans = 0
    bank = None
    designs = []
    with open('input.txt', 'r') as f:
        for line in f:
            if bank is None:
                # bank = sorted([line.strip().split(', ')])
                bank = set(line.strip().split(', '))
            elif len(line.strip()) > 0:
                designs.append(line.strip())
    
    for d in designs:
        if test_design(d, bank):
            ans += 1

    print(ans)

def test_design(design, bank):
    max_len = max(len(x) for x in bank)
    cache = {}
    def test_rec(design, bank, i):
        if i == len(design):
            return True
        if i in cache:
            return cache[i]
        chars_left = len(design) - i

        for k in range(min(max_len, chars_left), 0, -1):
            seg = design[i:i+k]
            if seg in bank:
                if test_rec(design, bank, i+k):
                    cache[i] = True
                    return True
        
        cache[i] = False
        return False
    
    return test_rec(design, bank, 0)

def part2():
    ans = 0
    bank = None
    designs = []
    with open('input.txt', 'r') as f:
        for line in f:
            if bank is None:
                # bank = sorted([line.strip().split(', ')])
                bank = set(line.strip().split(', '))
            elif len(line.strip()) > 0:
                designs.append(line.strip())
    
    for d in designs:
        arrs = total_arrangements(d, bank)
        # print(arrs)
        ans += arrs

    print(ans)

def total_arrangements(design, bank):
    max_len = max(len(x) for x in bank)
    cache = {}
    def arrs_rec(design, bank, i):
        if i == len(design):
            return 1
        if i in cache:
            return cache[i]
        chars_left = len(design) - i

        arrs = 0
        for k in range(min(max_len, chars_left), 0, -1):
            seg = design[i:i+k]
            if seg in bank:
                arrs += arrs_rec(design, bank, i+k)
        
        cache[i] = arrs
        return arrs
    
    return arrs_rec(design, bank, 0)


# part1()
part2()