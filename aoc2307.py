DAY = 7
VERBOSE =  False
PART = "12"

def get_data(fname):
    with open(fname) as f:
        return f.read().split('\n')
    
fname = f'input23{DAY:02}.aoc'
print(f"Advent of code 2023, Day {DAY}")

data = get_data(fname)
# print(data)


def ctype(c):
    sc = set(c)
    if len(sc) == 1:  # Five of a kind
        return 7
    elif len(sc) == 2:  
        a, b = tuple(sc)
        if c.count(a) in [1, 4]:  # Four of a kind
            return 6
        else:  # Full house
            return 5
    elif len(sc) == 3:
        a, b, x = sorted(c.count(i) for i in sc)
        if x == 3:  # Three
            return 4
        else:  # Two pair
            return 3
    elif len(sc) == 4:  # One pair
        return 2
    else:  # High
        return 1


chdict = {'A': 'e', 'K': 'd', 'Q': 'c', 'J': 'b', 'T': 'a'}
games = []
for d in data:
    c, v = d.split()
    rc = ctype(c)
    v = int(v)

    c = ''.join(chdict.get(k, k) for k in c)
    val = 1e6*rc + int(c, 16)
    games.append((val, v))
    # print(c, '->', 1e6*rc + int(c, 16), rc, v)

winnings = 0
rank = 1
for c, b in sorted(games):
    winnings += b * rank
    rank += 1

print('Part 1', winnings)


def joker_rule(c):
    order = 'AKQT' + ''.join(str(i) for i in range(9, 1, -1)) + 'J'
    if 'J' in c:
        ct = ctype(c)
        if ct == 7:
            return 'AAAAA'
        elif ct > 4:
            j = set(c) ^ set('J')
            return ''.join(j)*5
        elif ct == 4:
            if c.count('J') == 3:
                idx = min([order.index(i) for i in set(c) ^ set('J')])
                card = order[idx]
                return c.replace('J', card)
            else:
                for card in set(c) ^ set('J'):
                    if c.count(card) == 3:
                        return c.replace('J', card)
        elif ct > 1:
            tmp = c.replace('J', '')
            if len(tmp) == 6 - ct:
                for card in tmp:
                    if c.count(card) == 2:
                        return c.replace('J', card)
            else:
                idx = min(order.index(i) for i in set(tmp))
                card = order[idx]
                return c.replace('J', card)
        elif ct == 1:
            tmp = c.replace('J', '')
            idx = min(order.index(i) for i in set(tmp))
            card = order[idx]
            return c.replace('J', card)

    return c


chdict = {'A': 'd', 'K': 'c', 'Q': 'b', 'J': '1', 'T': 'a'}
games = []
for d in data:
    c, v = d.split()
    newc = joker_rule(c)
    rc = ctype(newc)
    v = int(v)

    c = ''.join(chdict.get(k, k) for k in c)
    val = 1e6*rc + int(c, 16)
    games.append((val, v))
    # print(c, '->', 1e6*rc + int(c, 16), rc, v)

winnings = 0
rank = 1
for c, b in sorted(games):
    winnings += b * rank
    rank += 1

print('Part 2', winnings)