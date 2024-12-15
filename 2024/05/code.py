def part1():
    ans = 0

    graph = {}
    updates = []
    with open('input.txt', 'r') as f:
        for line in f:
            chars = line.strip()
            if chars == '':
                continue
            elif len(chars) == 5:
                n1,n2 = int(chars[:2]),int(chars[-2:])
                if n1 not in graph:
                    graph[n1] = []
                if n2 not in graph:
                    graph[n2] = []
                graph[n1].append(n2)
            else:
                updates.append([int(x) for x in chars.split(',')])
    
    # could be faster with sets.
    after = graph

    # apparently this is cyclic so the below is a bad idea
    # after = {x:set(graph[x]) for x in graph}
    # done_updating = False
    # while not done_updating:
    #     done_updating = True
    #     for n in graph:
    #         before_update = len(after[n])
    #         for a in graph[n]:
    #             after[n] |= after[a]
    #         if len(after[n]) != before_update:
    #             done_updating = False
    # for n in sorted([x for x in graph]):
    #     print(n, after[n])

    for update in updates:
        valid = True
        for j in range(len(update)):
            for i in range(j):
                ni,nj = update[i],update[j]
                if ni in after[nj]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            mid = len(update) // 2
            ans += update[mid]

    print(ans)

def part2():
    ans = 0

    graph = {}
    updates = []
    with open('input.txt', 'r') as f:
        for line in f:
            chars = line.strip()
            if chars == '':
                continue
            elif len(chars) == 5:
                n1,n2 = int(chars[:2]),int(chars[-2:])
                if n1 not in graph:
                    graph[n1] = []
                if n2 not in graph:
                    graph[n2] = []
                graph[n1].append(n2)
            else:
                updates.append([int(x) for x in chars.split(',')])

    for update in updates:
        valid = True
        for j in range(len(update)):
            for i in range(j):
                ni,nj = update[i],update[j]
                if ni in graph[nj]:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            correct_update = correct_order(update, graph)
            mid = len(correct_update) // 2
            ans += correct_update[mid]

    print(ans)

def correct_order(update, graph):
    after = {x:[] for x in update}
    for ni in update:
        for nj in update:
            if nj in graph[ni]:
                after[ni].append(nj)
    
    order = sorted((len(after[x]),x) for x in after)
    return [x[1] for x in order]

    # print({x: len(after[x]) for x in after}) # <- this reveals that everything has a direct relation. thank goodness
    # print(sorted(len(after[x]) for x in after))

# part1()
part2()