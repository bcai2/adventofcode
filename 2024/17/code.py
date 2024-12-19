# from utils import utils
import re, heapq

def part1():
    ans = 0
    regs = [None, None, None]
    program = []
    with open('input.txt', 'r') as f:
        for line in f:
            if 'A' in line:
                regs[0] = int(re.sub(r'[^\-\d]+', '', line))
            elif 'B' in line:
                regs[1] = int(re.sub(r'[^\-\d]+', '', line))
            elif 'C' in line:
                regs[2] = int(re.sub(r'[^\-\d]+', '', line))
            elif len(line.strip()) == 0:
                continue
            else:
                program = [int(x) for x in re.split(r'[^\-\d]+', line) if len(x) > 0]
    
    ans = run_program(regs, program)
    print(ans)

def run_program(regs, program):
    output = []
    i = 0
    while i < len(program)-1:
        advance_normally = True
        inst = program[i]
        literal_operand = program[i+1]
        combo = literal_operand
        if 4 <= combo <= 6:
            combo = regs[literal_operand-4]

        if inst == 0:
            regs[0] //= 2**combo
        elif inst == 1:
            regs[1] ^= literal_operand
        elif inst == 2:
            regs[1] = combo % 8
        elif inst == 3:
            if regs[0] != 0:
                i = literal_operand
                advance_normally = False
        elif inst == 4:
            regs[1] ^= regs[2]
        elif inst == 5:
            output.append(combo % 8)
        elif inst == 6:
            regs[1] = regs[0] // 2**combo
        elif inst == 7:
            regs[2] = regs[0] // 2**combo
        
        if advance_normally:
            i += 2

    # print(regs)
    # print(program)

    ans = ','.join([str(o) for o in output])
    return ans

def part2():
    ans = 0
    regs = [None, None, None]
    program = []
    with open('input.txt', 'r') as f:
        for line in f:
            if 'A' in line:
                regs[0] = int(re.sub(r'[^\-\d]+', '', line))
            elif 'B' in line:
                regs[1] = int(re.sub(r'[^\-\d]+', '', line))
            elif 'C' in line:
                regs[2] = int(re.sub(r'[^\-\d]+', '', line))
            elif len(line.strip()) == 0:
                continue
            else:
                program = [int(x) for x in re.split(r'[^\-\d]+', line) if len(x) > 0]
    
    # program decoded manually
    possibilities = []
    bits = [-1]*48
    def search_rec(bits, i):
        if i == len(program):
            value = 0
            # print(bits)
            for idx,b in enumerate(bits):
                value += b * 2**idx
            possibilities.append(value)
            return
        
        target = program[i]

        options = [[0,1] if bits[x] == -1 else [bits[x]] for x in range(3*i,3*(i+1))]
        first_three_set_bits = []
        for k in range(3):
            if bits[3*i+k] == -1:
                first_three_set_bits.append(k)
        for o1 in options[0]:
            for o2 in options[1]:
                for o3 in options[2]:
                    set_bits = []
                    for k in first_three_set_bits:
                        o = [o1, o2, o3][k]
                        set_bits.append(3*i+k)
                        bits[3*i+k] = o
                    
                    b_val = o1 + 2 * o2 + 4 * o3
                    c_offset = 7 - b_val

                    c_val = target ^ b_val
                    c1 = c_val % 2
                    c2 = (c_val // 2) % 2
                    c3 = c_val // 4

                    c_valid = True
                    for idx,c_bit in zip([3*i+c_offset+x for x in range(3)], [c1, c2, c3]):
                        cur_bit = bits[idx] if idx < len(bits) else 0
                        if cur_bit == -1:
                            bits[idx] = c_bit
                            set_bits.append(idx)
                        elif cur_bit != c_bit:
                            c_valid = False
                            break

                    if c_valid:
                        search_rec(bits, i+1)
                    
                    for idx in set_bits:
                        bits[idx] = -1

    search_rec(bits, 0)
    # print(regs)
    # print(program)

    # print(possibilities)
    for p in possibilities:
        out = run_program([p, 0, 0], program)
        print(p, out)
    ans = min(possibilities)
    print(ans)

# part1()
part2()