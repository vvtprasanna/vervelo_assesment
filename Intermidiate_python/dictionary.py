#Dict

my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)

name_in_dict = my_dict["name"]
print(name_in_dict)

my_dict["email"] = "max@xyz.com"
print(my_dict)

my_dict["email"] = "coolmax@xyz.com"
print(my_dict)

print("popped value:", my_dict.pop("age"))

if "name" in my_dict:
    print(my_dict["name"])

for key, value in my_dict.items():
    print(key, value)

my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)