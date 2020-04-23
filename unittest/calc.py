
def add(x, y):
    """ Add Function """
    return x + y

def subtract(x, y):
    """ Subtract Function """
    return x - y

def multiply(x, y):
    """ Multiply Function """
    return x * y

def divide(x, y):
    """ Divide Function """
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

""" If you're going to work on any large projects then you're going to know how to properly write tests
    and the reason for that it is going to save a lot of time and headache down the road.
    So when you write good test for your code it gives you more confidence that your updates and refactoring
    don't have any unintended consequences or break your code in any way.
    For example: If you update a function in your project those changes may have actually broken 
    several sections of your code even in that function is still working and
    Good unit test will make sure that everything is still working as it should and if it's not
    then it will show you exactly what's broken """
