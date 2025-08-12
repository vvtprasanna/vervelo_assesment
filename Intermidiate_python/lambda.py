#lambda function

f = lambda x: x+10
val1 = f(5)
val2 = f(100)
print(val1, val2)
points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key= lambda x: x[1])
print(sorted_by_y)
a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))

print(b)
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))

print(b)