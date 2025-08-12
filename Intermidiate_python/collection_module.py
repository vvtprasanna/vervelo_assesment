#Collections

from collections import *
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())

Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)

ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
print(ordinary_dict)

d = defaultdict(int)
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])

d = deque()

d.append('a')
d.append('b')
print(d)

d.appendleft('c')
print(d)