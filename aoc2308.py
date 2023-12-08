import sys, os

DAY = 8
VERBOSE =  False
PART = "12"
print(f"Advent of code 2023, Day {DAY}")

with open(os.path.basename(sys.argv[0]).replace('py', 'in')) as f:
    data = f.read().split('\n')
# print(data)

# parse data
# lr -> movements
# dmap -> desert map as dict
lr = [int(i) for i in data[0].replace('L', '0').replace('R', '1')]
_ = [d.split(' = ') for d in  data[2:]]
# print(_); exit()
dmap = {el[0]: el[1][1:-1].split(', ') for el in _}
# print(lr, dmap)

if '1' in PART:
    start, end = 'AAA', 'ZZZ'
    loc = start
    i = 0
    while True:
        loc = dmap[loc][lr[i % len(lr)]]
        if loc == end:
            break
        i += 1
        if i % 1000 == 0: print(i, loc, end='\r')
    print('part 1:', i+1)


from math import lcm
start = [k for k in dmap if k[-1] == 'A']
# print(start); exit()
odp2 = 1
for s in start:
    
    loc = s
    i = 0
    while True:
        loc = dmap[loc][lr[i % len(lr)]]
        if loc[-1] == 'Z':
            break
        i += 1
    #     if i % 1000 == 0: print(i+1, loc, end='\r')
    # print(s, i+1, loc)
    odp2 = lcm(odp2, i+1)

print('part 2:', odp2)
