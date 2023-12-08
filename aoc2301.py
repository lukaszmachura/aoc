DAY = 1

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def get_first_number(s: str):
    for el in s:
        if el.isdecimal():
            return el
        

## replace names with numbers
def replace_names_with_numbers(s: str, d: dict):
    lengths = (3, 4, 5, 6)

    # first half
    stop = False
    for idx, el in enumerate(s):
        if el.isdecimal():
            break
        for l in lengths:
            chunk = s[idx:idx+l]
            if chunk in d:
                s = s[:idx] + str(d[chunk]) + s[idx+l:]
                stop = True
                break
        if stop:
            break

    # second half
    d = {k[::-1]: v for k, v in d.items()}
    s = s[::-1]
    stop = False
    for idx, el in enumerate(s):
        if el.isdecimal():
            break
        for l in lengths:
            chunk = s[idx:idx+l]
            if chunk in d:
                s = s[:idx] + str(d[chunk]) + s[idx+l:]
                stop = True
                break
        if stop:
            break
    
    return s[::-1]


fname = f'aoc23{DAY:02}.in'
print(f"Advent of code 2023, Day {DAY}")


with open(fname) as f:
    lines = f.readlines()

sum_cval = 0
for line in lines:
    n1 = get_first_number(line)
    n2 = get_first_number(line[::-1])
    sum_cval += int(n1+n2)

print('part 1: ', sum_cval)


# part 2


sum_cval = 0
for line in lines:
    newline = replace_names_with_numbers(line, numbers)
    n1 = get_first_number(newline)
    n2 = get_first_number(newline[::-1])
    n1n2 = n1 + n2
    sum_cval += int(n1n2)

print('part 2: ', sum_cval)
