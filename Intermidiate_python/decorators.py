#Decorators

def start_end_decorator(func):
    
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')
    
print_name()

def start_end_decorator_2(func):
    
    def wrapper(x):
        print('Start')
        result=func(x)
        print(result)
        print('End')
    return wrapper

@start_end_decorator_2
def add_5(x):
    return x + 5

print(add_5(10))
