#Lists

list_1 = ["banana", "cherry", "apple"]
print(list_1)

item = list_1[0]
print(item)

list_1[2] = "lemon"
print(list_1)

print("Length:", len(list_1))

my_list = ["banana", "cherry", "apple"]
my_list.reverse()
print('Reversed: ', my_list)

my_list.remove("cherry") 
print(my_list)

list_with_zeros = [0] * 5
print(list_with_zeros)

for i in list_1:
    print(i)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] 
print(b)

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [i * i for i in a]
print(y)