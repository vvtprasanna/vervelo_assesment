#String

my_string = "Hello World"

b = my_string[0]
print(b)

b = my_string[1:3] 
print(b)

my_string = "     Hello World "


my_string = my_string.strip()
print(my_string)


print(len(my_string))


print(my_string.upper())
print(my_string.lower())

print("hello".startswith("he"))
print("hello".endswith("llo"))

print("Hello".count("e"))

my_string = "one,two,three"
a = my_string.split(",")
print(a)
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) 
print(a)