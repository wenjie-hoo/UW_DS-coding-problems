import itertools
from numpy import var
import pulp
import string


def covered(tile, base):
    return {(base[0] + t[0], base[1] + t[1]): True for t in tile}

tiles = [[(0,0), (1,0), (1,1), (0,1)],
         [(0,0), (2,0), (2,2), (0,2)],
         [(0,0), (3,0), (3,3), (0,3)],
         [(0,0), (4,0), (4,4), (0,4)],
         [(0,0), (5,0), (5,5), (0,5)],
        #  [(0,0), (6,0), (6,6), (0,6)],
        #  [(0,0), (7,0), (7,7), (0,7)],
        #  [(0,0), (8,0), (8,8), (0,8)],
        #  [(0,0), (9,0), (9,9), (0,9)],
        #  [(0,0), (10,0), (10,10), (0,10)],
        #  [(0,0), (11,0), (11,11), (0,11)],
        #  [(0,0), (12,0), (12,12), (0,12)],
        #  [(0,0), (13,0), (13,13), (0,13)],
        #  [(0,0), (14,0), (14,14), (0,14)],
        #  [(0,0), (15,0), (15,15), (0,15)],
        #  [(0,0), (16,0), (16,16), (0,16)],
        #  [(0,0), (17,0), (17,17), (0,17)],
        #  [(0,0), (18,0), (18,18), (0,18)],
        #  [(0,0), (19,0), (19,19), (0,19)],
        #  [(0,0), (20,0), (20,20), (0,20)],
        ]
rows = 10
cols = 10
squares = {x: True for x in itertools.product(range(rows), range(cols))}
# print(squares)
vars = list(itertools.product(range(rows), range(cols), range(len(tiles))))

vars = [x for x in vars if all([y in squares for y in covered(tiles[x[2]], (x[0], x[1])).keys()])]
# print(vars)
x = pulp.LpVariable.dicts('tiles', vars, lowBound=0, upBound=1, cat=pulp.LpInteger)
mod = pulp.LpProblem('polyominoes', pulp.LpMaximize)
mod += sum([len(tiles[p[2]]) * x[p] for p in vars])
for tnum in range(len(tiles)):
    mod += sum([x[p] for p in vars if p[2] == tnum]) <= 1
# Each square can be covered by at most one shape
for s in squares:
    mod += sum([x[p] for p in vars if s in covered(tiles[p[2]], (p[0], p[1]))]) <= 1
# Solve and output
mod.solve()
out = [['-'] * cols for rep in range(rows)]
chars = string.ascii_uppercase + string.ascii_lowercase
numset = 0
for p in vars:
    if x[p].value() == 1.0:
        for off in tiles[p[2]]:
            out[p[0] + off[0]][p[1] + off[1]] = chars[numset]
        numset += 1
for row in out:
    # print(row)
    print(''.join(row))

