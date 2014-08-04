#From http://rosettacode.org/wiki/N-queens_problem#Python

from itertools import permutations
 
n = 8

cols = range(n)
soloves = []
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \
         == len(set(vec[i]-i for i in cols)):
        lo = list(vec)
        print ( list(vec) )
        soloves.append([str(x+1) for x in lo])

for l in soloves:
  print ( "".join(l))