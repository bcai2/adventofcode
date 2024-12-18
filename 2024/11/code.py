def part1():
    ans = 0
    config = []
    with open('input.txt', 'r') as f:
        for line in f:
            config = [int(x) for x in line.strip().split()]

    for _ in range(25):
        new_config = []
        for n in config:
            if n == 0:
                new_config.append(1)
            else:
                s = str(n)
                if len(s) % 2 == 0:
                    new_config.append(int(s[:len(s)//2]))
                    new_config.append(int(s[len(s)//2:]))
                else:
                    new_config.append(2024*n)
        config = new_config
    
    ans = len(config)

    print(ans)

from collections import defaultdict
def part2():
    ans = 0
    config = []
    with open('input.txt', 'r') as f:
        for line in f:
            config = [int(x) for x in line.strip().split()]

    config_dict = {}
    for n in config:
        if n not in config_dict:
            config_dict[n] = 0
        config_dict[n] += 1
    config = config_dict

    for k in range(75):
        print(k)
        # print(config)
        new_config = defaultdict(int)
        for n in config:
            if n == 0:
                new_config[1] += config[n]
            else:
                s = str(n)
                if len(s) % 2 == 0:
                    new_config[int(s[:len(s)//2])] += config[n]
                    new_config[int(s[len(s)//2:])] += config[n]
                else:
                    new_config[2024*n] += config[n]
        config = new_config
    
    print(len(config))
    ans = sum(config[n] for n in config)

    print(ans)

# part1()
part2()