a = [1, 2, 3, 4]
b = 'sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

# The goal of __repr__ is to be unambiguous
# made for developers to easily figure out detail about the variable

# The goal of __str__ is to be readable
# user friendly targeted non-developers

""" str(object) returns object.__str__(), which is the “informal” or nicely printable string representation of object. 
    For string objects, this is the string itself. If object does not have a __str__() method, 
    then str() falls back to returning repr(object). """