def part1():
    list1 = []
    list2 = []
    with open('input.txt', 'r') as f:
        for line in f:
            a,b = (int(x) for x in line.split())
            list1.append(a)
            list2.append(b)

    list1, list2 = sorted(list1), sorted(list2)

    diff = 0
    for a,b in zip(list1, list2):
        diff += abs(b-a)

    print(diff)

def part2():
    list1 = []
    list2 = {}
    with open('input.txt', 'r') as f:
        for line in f:
            a,b = (int(x) for x in line.split())
            list1.append(a)
            if b not in list2:
                list2[b] = 0
            list2[b] += 1

    score = 0
    for a in list1:
        if a not in list2:
            continue
        score += list2[a] * a

    print(score)

# part1()
part2()