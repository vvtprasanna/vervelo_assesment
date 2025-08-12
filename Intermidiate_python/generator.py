#Generators


def firstn1(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n1 = sum(firstn1(1000000))
print(sum_of_first_n1)


def firstn2(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n2 = sum(firstn2(1000000))
print(sum_of_first_n2)



def fibonacci(limit):
    a, b = 0, 1 
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)

print(list(fib))