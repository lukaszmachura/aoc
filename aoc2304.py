import sys, os
DAY = 4

VERBOSE =  False
PART = "12"


def only_empty_lists(L):
    return all(not el for el in L)


def get_data(fname):
    ret = {}
    with open(fname) as f:
        for line in f:
            if VERBOSE: print(line)
            key, val = line.split(': ')
            key = int(key.split()[1])
            win, card = val.split(' | ')
            win = [int(n) for n in win.split()]
            card = [int(n) for n in card.split()]
            ret[key] = (win, card)
    return ret

fname = f'aoc23{DAY:02}.in'
print(f"Advent of code 2023, Day {DAY}")

cards = get_data(fname)
# print(cards)

if '1' in PART:
    wins_per_card = {}
    points = 0
    for key, val in cards.items():
        if VERBOSE: print(key, val)
        win, card = val 
        win_num = sum(1 for c in card if c in win)
        wins_per_card[key] = win_num
        if win_num:
            points += 1 << win_num - 1
    print('part 1: ', points)


if '2' in PART:
    if VERBOSE: print(wins_per_card)
    # change wins into cards
    extra = {
        k: list(range(k + 1, k + v + 1)) 
        for k, v in wins_per_card.items()
        }
    
    last = len(cards)
    while last > 0:
        if extra[last] == []:
            extra[last] = 1
        else:
            extra[last] = sum(extra[idx] for idx in extra[last]) + 1
        last -= 1

    number_of_all_cards = sum(extra.values())
    print('part 2: ', number_of_all_cards)