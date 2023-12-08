DAY = 3

VERBOSE = False
PART = "12"

def get_data(fname):
    with open(fname) as f:
        ret = f.readlines()
    ret = [el.strip() for el in ret]
    return ret


def scan_line_for_numbers(line):
    ret = []
    number = ''
    indices = []
    for idx, n in enumerate(line):
        if n.isdecimal():
            number += n
            indices.append(idx)
        else:
            if number:
                ret.append((int(number), indices[0], indices[-1]))
            number = ''
            indices = []
    if number:
        ret.append((int(number), indices[0], indices[-1]))

    return ret


def get_line_chunk(lidx, start, stop, engine):
    return engine[lidx][start:stop+1]


def is_part_number(num, lidx, engine):
    n, start, stop = num
    
    envelope = ''
    if start:
        start -= 1
        envelope += engine[lidx][start]
        if VERBOSE: print('left OK', end='..')

    if stop < len(engine[lidx]) - 1:
        stop += 1
        envelope += engine[lidx][stop]
        if VERBOSE: print('right OK', end='..')
    
    if lidx > 0:
        envelope += get_line_chunk(lidx-1, start, stop, engine)
        if VERBOSE: print('above OK', end='..')
    
    if lidx < len(engine) - 1:
        envelope += get_line_chunk(lidx+1, start, stop, engine)
        if VERBOSE: print('below OK', end='..')

    return True if len(set(envelope)) > 1 else False
    

def scan_line_for_symbol(line, symbol='*'):
    ret = ()
    for idx, el in enumerate(line):
        if el == symbol:
            ret += (idx, )
    return ret


def gear_ratio(sidx, lineidx, engine):
    beside_nums = []

    # same line
    nums = scan_line_for_numbers(engine[lineidx])
    if nums:
        for n, a, b in nums:
            if b == sidx - 1:
                beside_nums.append(n)
            if a == sidx + 1:
                beside_nums.append(n)

    # above
    for shift in [-1, 1]:
        if lineidx > 0:
            nums = scan_line_for_numbers(engine[lineidx+shift])
            if nums:
                for n, a, b in nums:
                    lenn = b - a + 1
                    if (a >= sidx - lenn) and (b <= sidx + lenn):
                        beside_nums.append(n)

    ret = beside_nums[0] * beside_nums[1] if len(beside_nums) == 2 else 0
    return ret

fname = f'aoc23{DAY:02}.in'
print(f"Advent of code 2023, Day {DAY}")

engine = get_data(fname)
# print(engine)

if "1" in PART:
    sum_part_no = 0
    for lineidx, line in enumerate(engine):
        # if lineidx != len(engine) - 66 - 20: continue
        numbers = scan_line_for_numbers(line)
        if numbers:
            for num in numbers:
                if VERBOSE: print(num, end=" -> ")
                if is_part_number(num, lineidx, engine):
                    if VERBOSE: print('Tak')
                    sum_part_no += num[0]
                else:
                    if VERBOSE: print('...Nie...')

    print('part 1: ', sum_part_no)

if "2" in PART:
    if VERBOSE: print("*" * 33)
    sum_gear = 0
    for lineidx, line in enumerate(engine):
        # if lineidx != len(engine) - 66 - 20: continue
        stars = scan_line_for_symbol(line)
        if stars:
            for sidx in stars:
                gr = gear_ratio(sidx, lineidx, engine)
                if VERBOSE: print(lineidx, sidx, gr)
                sum_gear += gr

    print('part 2: ', sum_gear)