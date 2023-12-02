DAY = 2


def get_number(s: str):
    no = ''
    for x in s:
        if x.isdecimal():
            no += x
    return int(no)


def get_games(fname):
    ret = {}
    with open(fname) as f:
        for line in f:
            key, val = line.split(': ')
            ret[get_number(key)] = val.strip()
    return ret


def is_game_possible(game, bag):
    game = game.replace(';', ',')
    cubes = game.split(',')
    for cube in cubes:
        for color, maxballs in bag.items():
            if color in cube and get_number(cube) > maxballs:
                return False
    return True


def calculate_game_power(game, bag):
    game = game.replace(';', ',')
    cubes = game.split(',')
    max_color = dict.fromkeys(bag.keys(), ())
    for cube in cubes:
        for color in bag:
            if color in cube:
                max_color[color] += (get_number(cube), )
    power = 1
    for k, v in max_color.items():
        power *= max(v)
    return power


fname = f'input23{DAY:02}.aoc'
print(f"Advent of code 2023, Day {DAY}")

bag = {'red': 12, 'green': 13, 'blue': 14}
games = get_games(fname)

# pat 1
idsum = 0
for num in games:
    game = games[num]
    if is_game_possible(game, bag):
        idsum += num

print('part 1: ', idsum)

# part 2
total_power = 0
for num, game in games.items():
    power = calculate_game_power(game, bag)
    total_power += power

print('part 2: ', total_power)