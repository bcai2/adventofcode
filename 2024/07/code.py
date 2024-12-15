def part1():
    ans = 0
    with open('input.txt', 'r') as f:
        for line in f:
            num_data = line.strip().split()
            target = int(num_data[0][:-1])
            nums = [int(x) for x in num_data[1:]]
            values = [nums[0]]
            for n in nums[1:]:
                new_values = set()
                for v in values:
                    if v+n <= target:
                        new_values.add(v+n)
                    if v*n <= target:
                        new_values.add(v*n)
                values = new_values
            if target in values:
                ans += target
            
    print(ans)

def part2():
    ans = 0
    with open('input.txt', 'r') as f:
        for line in f:
            num_data = line.strip().split()
            target = int(num_data[0][:-1])
            nums = [int(x) for x in num_data[1:]]
            values = [nums[0]]
            for n in nums[1:]:
                new_values = set()
                for v in values:
                    if v+n <= target:
                        new_values.add(v+n)
                    if v*n <= target:
                        new_values.add(v*n)
                    if int(str(v) + str(n)) <= target:
                        new_values.add(int(str(v) + str(n)))
                values = new_values
            if target in values:
                ans += target
            
    print(ans)

# part1()
part2()