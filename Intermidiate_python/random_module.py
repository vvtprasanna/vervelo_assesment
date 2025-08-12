#Random Numbers

import random


a = random.random()
print(a)

a = random.uniform(1,10)
print(a)

a = random.randint(1,10)
print(a)

a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

random.seed(1)
print(random.random())
random.seed(1)
print(random.random())
