from __future__ import print_function
from plays import play


with open('rules.csv', 'r') as f:
    for l in f:
        hand = map(lambda string: int(string), l.split(','))
        v = play(hand)
        print(l.rstrip() + ',' + v)


