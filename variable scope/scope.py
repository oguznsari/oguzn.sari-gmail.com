"""
LEGB -- Local, Enclosing, Global, Built-in

Local -- variables defined within a function
Global -- variables defined at the top level of a module or explicitly declared global using the global keyword
Built-ins -- names that are pre-assigned in Python
Enclosing -- has to do with nested functions
"""

# x = 'global x'

# import builtins
# print(dir(builtins))                    # a lot of builtins are exceptions and error names
#
# def my_min():
#     pass
#
# m = min([5, 1, 4, 2, 3])                # min() -- built-in function
# print(m)

def test(z):
    # y = 'local y'
    # print(y)

    global x
    x = 'local x'
    print(x)                # LEGB -L
    print(z)

test('local z')
print(x)                    # LEGB -G


# Enclosing
def outer():
    x = 'outer x'

    def inner():
        # nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)