import sys, os

DAY = 9
VERBOSE =  False
PART = "12"
print(f"Advent of code 2023, Day {DAY}")

with open(os.path.basename(sys.argv[0]).replace('py', 'in')) as f:
    data = f.read().split('\n')
# print(data)

oasis = [
    list(map(int, line.split())) for line in data
]
# print(oasis)

# 1

def pred_phase1(L):
    ret = [L]
    buf = [1]
    while any(buf):
        buf = []
        for idx in range(len(ret[-1])-1):
            buf.append(ret[-1][idx+1] - ret[-1][idx])
        ret.append(buf)
    return ret

def pred_phase2a(pp1):
    ret = 0
    for line in pp1[::-1]:
        ret += line[-1]
    return ret

def pred_phase2b(pp1):
    p = pp1[::-1]
    x = 0
    for idx, line in enumerate(p[:-1]):
        x = p[idx+1][0] - x
    # print(x)
    return x

odp1 = odp2 = 0
for line in oasis:
    # print(line)
    pp1 = pred_phase1(line)
    odp1 += pred_phase2a(pp1)
    odp2 += pred_phase2b(pp1)
print('Part 1: ', odp1)
print('Part 2: ', odp2)