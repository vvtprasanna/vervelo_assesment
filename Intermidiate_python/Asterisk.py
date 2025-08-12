#*

result = 7 * 5
print(result)


result = 2 ** 4
print(result)

A_string = "A" * 10
AB_string = "AB" * 5
print(A_string)
print(AB_string)


my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
my_list = [*my_tuple, *my_set]
print(my_list)

dict_a = {'one': 1, 'two': 2}
dict_b = {'three': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)