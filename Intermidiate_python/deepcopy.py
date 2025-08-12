#deepcopy

import copy

list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)

list_a[0][0]= -10
print(list_a)
print(list_b)