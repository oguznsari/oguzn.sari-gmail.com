""" Instead of using print statements we will use very basic logging
    setting different logging levels
    log information to files

    Default level of logging is set to WARNING -- capture everything that is a WARNING
    or above (WARNING + ERROR + DEBUG) """
import logging

"""
DEBUG: Detailed information, typically of interest only when diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative of some problem in the future
          (e.g 'disc space low'). The software still working as expected.
          
ERROR: Due to more serious problem, the software has not been able to perform some function.

CRITICAL: A serious error, indicating that the program itself may be unable to continue running. """

logging.basicConfig(filename='test.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')           # asctime:levelname:message

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))


sub_result = subtract(num_1, num_2)
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
# logging.warning('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))


mul_result = multiply(num_1, num_2)
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
# logging.warning('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))


div_result = divide(num_1, num_2)
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
# logging.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))


# DEBUG and INFO doesn't log anything to your console and that's because default logging level is WARNING
# It is only going to log out WARNINGs and higher
# can change it via basicConfig

""" default format LOGLEVEL:logger:message --> to see what is available check below link
    https://docs.python.org/3/library/logging.html#logrecord-attributes """