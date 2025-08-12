#Tuple

tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" 

tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)

tuple_4 = tuple([1,2,3])
print(tuple_4)

item = tuple_1[-1]
print(item)

my_tuple = ('a','p','p','l','e',)


print(len(my_tuple))

print(my_tuple.count('p'))

print(my_tuple.index('l'))

tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name)
print(age)
print(city)