def part1():
    ans = 0
    with open('input.txt', 'r') as f:
        for line in f:
            mul_tracker = 0
            digits = []
            val1 = 0
            for c in line:
                if c == 'm':
                    mul_tracker = 1
                elif c == 'u' and mul_tracker == 1:
                    mul_tracker = 2
                elif c == 'l' and mul_tracker == 2:
                    mul_tracker = 3
                elif c == '(' and mul_tracker == 3:
                    mul_tracker = 4
                elif c.isdigit() and mul_tracker == 4:
                    digits.append(c)
                elif c == ',' and mul_tracker == 4 and len(digits) >= 1 and len(digits) <= 3:
                    mul_tracker = 5
                    val1 = int(''.join(digits))
                    digits = []
                elif c.isdigit() and mul_tracker == 5:
                    digits.append(c)
                elif c == ')' and mul_tracker == 5 and len(digits) >= 1 and len(digits) <= 3:
                    mul_tracker = 0
                    val2 = int(''.join(digits))
                    ans += val1 * val2
                else:
                    mul_tracker = 0
                
                if mul_tracker < 4:
                    digits = []
                    val1 = 0

    print(ans)

def part2():
    ans = 0
    with open('input.txt', 'r') as f:
        enabled = True
        for line in f:
            flip_tracker = 0
            mul_tracker = 0
            digits = []
            val1 = 0
            for c in line:
                if enabled:
                    if c == 'd':
                        flip_tracker = 1
                    elif c == 'o' and flip_tracker == 1:
                        flip_tracker = 2
                    elif c == 'n' and flip_tracker == 2:
                        flip_tracker = 3
                    elif c == '\'' and flip_tracker == 3:
                        flip_tracker = 4
                    elif c == 't' and flip_tracker == 4:
                        flip_tracker = 5                                                
                    elif c == '(' and flip_tracker == 5:
                        flip_tracker = 6
                    elif c == ')' and flip_tracker == 6:
                        flip_tracker = 0
                        enabled = False
                        mul_tracker = 0
                        digits = []
                        val1 = 0
                        continue
                    else:
                        flip_tracker = 0

                    if c == 'm':
                        mul_tracker = 1
                    elif c == 'u' and mul_tracker == 1:
                        mul_tracker = 2
                    elif c == 'l' and mul_tracker == 2:
                        mul_tracker = 3
                    elif c == '(' and mul_tracker == 3:
                        mul_tracker = 4
                    elif c.isdigit() and mul_tracker == 4:
                        digits.append(c)
                    elif c == ',' and mul_tracker == 4 and len(digits) >= 1 and len(digits) <= 3:
                        mul_tracker = 5
                        val1 = int(''.join(digits))
                        digits = []
                    elif c.isdigit() and mul_tracker == 5:
                        digits.append(c)
                    elif c == ')' and mul_tracker == 5 and len(digits) >= 1 and len(digits) <= 3:
                        mul_tracker = 0
                        val2 = int(''.join(digits))
                        # print(val1, val2)
                        ans += val1 * val2
                    else:
                        mul_tracker = 0
                    
                    if mul_tracker < 4:
                        digits = []
                        val1 = 0
                else:
                    if c == 'd':
                        flip_tracker = 1
                    elif c == 'o' and flip_tracker == 1:
                        flip_tracker = 2                               
                    elif c == '(' and flip_tracker == 2:
                        flip_tracker = 3
                    elif c == ')' and flip_tracker == 3:
                        flip_tracker = 0
                        enabled = True
                        continue
                    else:
                        flip_tracker = 0                        

    print(ans)

# part1()
part2()