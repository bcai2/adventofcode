def line_is_safe(nums):
    prev = nums[0]
    is_inc = (nums[1] - nums[0] > 0)
    is_safe = True

    for n in nums[1:]:
        if is_inc:
            if n <= prev:
                is_safe = False
        else:
            if n >= prev:
                is_safe = False
        diff = abs(n-prev)
        if diff < 1 or diff > 3:
            is_safe = False
        
        if not is_safe:
            break
        prev = n
    
    return is_safe

def part1():
    ans = 0
    with open('input.txt', 'r') as f:
        for line in f:
            nums = [int(x) for x in line.split()]
            is_safe = line_is_safe(nums)
            
            if is_safe:
                # print(line)
                ans += 1

    print(ans)

def part2():
    ans = 0
    with open('input.txt', 'r') as f:
        for line in f:
            nums = [int(x) for x in line.split()]
            if line_is_safe(nums):
                ans += 1
            else:
                # inefficient but works!
                for i in range(len(nums)):
                    nums_minus_i = nums[:i] + nums[i+1:]
                    if line_is_safe(nums_minus_i):
                        ans += 1
                        break

    print(ans)

part1()
part2()