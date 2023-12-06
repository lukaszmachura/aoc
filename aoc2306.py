DAY = 6
VERBOSE =  False
PART = "12"

def get_data(fname):
    with open(fname) as f:
        return f.read().split('\n')
    
fname = f'input23{DAY:02}.aoc'
print(f"Advent of code 2023, Day {DAY}")

data = get_data(fname)
# print(data)

times = [int(x.strip()) for x in data[0].split(':')[1].split()]
dist = [int(x) for x in data[1].split(':')[1].split()]
# print(times, dist)

part = 1
res = 1
for it, t in enumerate(times):
    beat = 0
    for sec in range(1, t+1):
        d = sec * (t-sec)  # v = sec
        if d > dist[it]:
            beat += 1
            # print(t, sec, d)
    res *= beat
print(f'PART {part}', res)

times = int(data[0].split(':')[1].replace(' ', ''))
dist = int(data[1].split(':')[1].replace(' ', ''))
# print(times, dist)

part = 2 
beat = 0
for sec in range(1, times+1):
    d = sec * (times-sec)  # v = sec
    if d > dist:
        beat += 1
        # print(t, sec, d)
res = beat
print(f'PART {part}', res)