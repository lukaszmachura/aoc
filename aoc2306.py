import sys, os

DAY = 6
VERBOSE =  False
PART = "12"
print(f"Advent of code 2023, Day {DAY}")

with open(os.path.basename(sys.argv[0]).replace('py', 'in')) as f:
    data = f.read().split('\n')
# print(data)


times = [int(x) for x in data[0].split(':')[1].split()]
dist = [int(x) for x in data[1].split(':')[1].split()]

p1 = 1
for t, d in zip(times, dist):
    p1 *= sum(1 for s in range(1, t+1) if s*(t-s) > d)
print(f'PART 1', p1)

t = int(data[0].split(':')[1].replace(' ', ''))
d = int(data[1].split(':')[1].replace(' ', ''))
p2 = sum(1 for s in range(1, t) if s*(t-s) > d)
print(f'PART 2', p2)