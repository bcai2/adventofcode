def part1():
    ans = 0

    pos = 0
    file_starts = []
    gaps = []
    is_file = True
    with open('input.txt', 'r') as f:
        for line in f:
            for c in line.strip():
                n = int(c)
                if is_file:
                    file_id = len(file_starts)
                    file_starts.append([pos, n])
                    
                    ans += (pos * n + (n-1) * n // 2) * file_id

                    pos += n
                    is_file = False
                else:
                    if n > 0:
                        gaps.append([pos, n])

                    pos += n
                    is_file = True

    # print(gaps)
    # print(file_starts)

    gap_idx = 0
    file_to_shift = len(file_starts)-1
    while gap_idx < len(gaps):
        fpos, fn = file_starts[file_to_shift]
        gpos, gn = gaps[gap_idx]
        if gpos > fpos:
            break
        if gn <= fn:
            diff = fn - gn
            ans -= (fpos + diff - gpos) * gn * file_to_shift
            gaps[gap_idx][1] = 0
            gap_idx += 1
            file_starts[file_to_shift][1] = diff
            if diff == 0:
                file_to_shift -= 1
        else:
            ans -= (fpos - gpos) * fn * file_to_shift
            gaps[gap_idx][1] -= fn
            gaps[gap_idx][0] += fn
            file_starts[file_to_shift][1] = 0
            file_to_shift -= 1

    # print(gaps)
    # print(file_starts)

    print(ans)

import heapq
def part2():
    ans = 0

    pos = 0
    file_starts = []
    gaps = {x:[] for x in range(1,10)}
    is_file = True
    with open('input.txt', 'r') as f:
        for line in f:
            for c in line.strip():
                n = int(c)
                if is_file:
                    file_id = len(file_starts)
                    file_starts.append([pos, n])
                    
                    ans += (pos * n + (n-1) * n // 2) * file_id

                    pos += n
                    is_file = False
                else:                    
                    if n > 0:
                        heapq.heappush(gaps[n], pos)
                    pos += n
                    is_file = True

    # print(gaps)
    # print(file_starts)

    file_to_shift = len(file_starts)-1
    while file_to_shift >= 0:
        fpos, fn = file_starts[file_to_shift]
        is_moved = False
        gpos = fpos
        gn = fn
        for k in range(fn,10):
            if len(gaps[k]) > 0 and gaps[k][0] < fpos and gaps[k][0] < gpos:
                gpos = gaps[k][0]
                gn = k
                is_moved = True
        if is_moved:
            ans -= (fpos - gpos) * fn * file_to_shift
            file_starts[file_to_shift][0] = gpos
            heapq.heappop(gaps[gn])
            diff = gn - fn
            if diff > 0:
                heapq.heappush(gaps[diff], gpos+fn)
        file_to_shift -= 1

    # print(gaps)
    # print(file_starts)

    print(ans)

# part1()
part2()