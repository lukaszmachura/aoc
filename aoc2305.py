DAY = 5
VERBOSE =  False
PART = "12"

def get_data(fname):
    with open(fname) as f:
        return f.read().split('\n')


def data_to_maps(data):
    data = data.copy()
    
    #seeds
    seeds = tuple(map(int, data.pop(0).split(': ')[1].split()))
    
    #maps
    maps = {}
    key, val = '', ()
    for line in data[1:]:
        if 'map' in line:
            key = line.split()[0]
        elif line == '':
            maps[key] = val
            val = ()
        else:
            val += (tuple(map(int, line.split())), )

    if line:
        maps[key] = val
    
    return seeds, maps


def find_destination_old(source, map):
    destination, sources = (), ()
    for m in map:
        map_range = m[2]
        destination += tuple(range(m[0], m[0]+map_range))
        sources += tuple(range(m[1], m[1]+map_range))

    if source in sources:
        # print(source, sources)
        return destination[sources.index(source)]
    else:
        # print(source)
        return source
    

def find_destination(source, map):
    dest = source
    for m in map:
        map_range = m[2]
        start, stop = m[1], m[1] + map_range
        if start <= source < stop:
            dest = m[0] + source - start
            break
    return dest


fname = f'input23{DAY:02}.aoc'
print(f"Advent of code 2023, Day {DAY}")

almanac = get_data(fname)
# print(almanac)

seeds, maps = data_to_maps(almanac)
# print(seeds, maps)

if "1" in PART:
    stages = ['seed-to-soil', 'soil-to-fertilizer', 
              'fertilizer-to-water', 'water-to-light', 
              'light-to-temperature', 'temperature-to-humidity', 
              'humidity-to-location'] #list(maps.keys())
    loc = []
    for seed in seeds:
        source = seed
        for stage in stages:
            dest = find_destination(source, maps[stage])
            source = dest
        loc.append(dest)
    print('Part 1: ', min(loc))


def prepare_seeds(seeds):
    new_seeds = ((seeds[0], seeds[1]), )
    idx = 2
    while idx < len(seeds):
        start = seeds[idx]
        stop = seeds[idx] + seeds[idx+1]
        for s in new_seeds:
            a, b = s[0], s[0] + s[1]
            if a <= start < b:
                start = b
            if a <= stop < b:
                stop = a
        new_seeds += ((start, stop-start), )
        idx += 2
    return new_seeds

if "2" in PART:
    # print(seeds, prepare_seeds(seeds), sep='\n'); exit()
    # loc = {}
    loc = 1e100
    sidx = 0
    while 1 and sidx < len(seeds):
        seed = seeds[sidx]
        slimit = seeds[sidx] + seeds[sidx+1]
        while seed < slimit:
            if seed % 10000 == 0: print((seed - seeds[sidx])/(slimit), end='\r')
            # if seed not in loc:
            source = seed
            for stage in stages:
                dest = find_destination(source, maps[stage])
                source = dest
            # loc[seed] = dest
            loc = min(loc, dest)
            seed += 1
        # break
        sidx += 2
    # print('Part 2: ', min(loc.values()))
    print('Part 2: ', loc)