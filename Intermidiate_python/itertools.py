#Itertools

from itertools import *

for i in count(10):
    print(i)
    if  i >= 13:
        break

perm = permutations([1, 2, 3])
print(list(perm))