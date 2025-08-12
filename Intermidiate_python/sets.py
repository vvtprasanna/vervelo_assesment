#Sets

my_set = {"apple", "banana", "cherry"}
print(my_set)

my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)

my_set = set()

my_set.add(42)
my_set.add(True)
my_set.add("Hello")
print(my_set)

my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

set_org = {1, 2, 3, 4, 5}

set_copy = set_org


set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

set_org = {1, 2, 3, 4, 5}
set_copy = set_org.copy()

set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)