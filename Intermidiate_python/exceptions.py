#Exceptions

try:
    a = 5 / 0
    w=2+"s"
except Exception as e:
    print(e)

class ValueTooHighError(Exception):
    pass

def test_value(a):
    if a > 1000:
        raise ValueTooHighError('Value is too high.')
    
    return a

try:
    test_value(1111)
except ValueTooHighError as e:
    print(e)
