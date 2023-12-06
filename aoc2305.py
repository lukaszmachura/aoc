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


def prepare_seeds(seeds):
    return [(seeds[idx], seeds[idx] + seeds[idx+1]) 
            for idx in range(0, len(seeds), 2)]


fname = f'input23{DAY:02}.aoc'
print(f"Advent of code 2023, Day {DAY}")

almanac = get_data(fname)
# print(almanac)

seeds, maps = data_to_maps(almanac)
stages = ['seed-to-soil', 'soil-to-fertilizer', 
          'fertilizer-to-water', 'water-to-light', 
          'light-to-temperature', 'temperature-to-humidity', 
          'humidity-to-location'] #list(maps.keys())


if "1" in PART:
    loc = []
    for seed in seeds:
        source = seed
        for stage in stages:
            dest = find_destination(source, maps[stage])
            source = dest
        loc.append(dest)
    print('Part 1: ', min(loc))

if "2" in PART:
    # change seeds from (start, range) into section (start, stop)
    seeds = prepare_seeds(seeds)
    for stage in stages:
        m = maps[stage]
        newseeds = []
        while seeds:
            ss, se = seeds.pop()
            for dest, src, ran in m:
                ms, me = src, src + ran
                os = max(ss, ms)  # overlap start
                oe = min(se, me)  # overlap end
                # if seed range overlap map
                if os < oe:
                    # overlap tranformation: seed + (dest - src)
                    newseeds.append((os - src + dest, oe - src + dest))
                    # left rest of seeds (if exist)
                    if ss < os:
                        seeds.append((ss, os))
                    # right rest of seeds
                    if oe < se:
                        seeds.append((oe, se))
                    break
            else:
                newseeds.append((ss, se))
        seeds = newseeds
            
    print('Part 2: ', min(seeds, key=lambda x: x[0])[0]) 
    # print('Part 2: ', sorted(seeds))



# --map, **seed
# ms-------------------------me
#        ss*********se
#        os         oe

#               ms-----------------------me
#        ss***********se
#               os    oe

# ms-----------------------me
#                   ss***********se
#                   os     oe

#                           ms-----------------------me
#        ss***********se
#                     os    oe

# ms-----------------------me
#                              ss***********se
#                          os  oe