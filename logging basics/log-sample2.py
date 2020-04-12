import logging
import employee2                # when we import a module it runs the code from that module when it's imported
                                # creates employees and log those but doesn't log below statements
                                # root logger already configured inside the imported employee2
                                # below doesn't overwrites initial configurations


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('log-sample2.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# we can add more than 1 handler to our formatter
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)


""" If we want to keep our loger level at DEBUG but only wanted ERRORs or worse to get logger;
    - keep logger level at DEBUG
    - set level on the file_handler
        file_handler.setLevel(logging.ERROR) """

# logging.basicConfig(filename='log-sample2.log', level=logging.DEBUG,
#     format='%(asctime)s:%(levelname)s:%(message)s')           # asctime:levelname:message

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
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero')         # traceback ** more information

    else:
        return result
    # return x / y


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
# logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
# logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result)
# logging.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

""" when change the level from debug to info we were able to log into employee2.log
    but we are not getting the log file that we want
    we are not getting the log levels that we want
    we are not getting the formatting that we want
    
    Get a new logger for each of our modules so that we can configure both of them seperately """


""" check Python documentation to dig into further;
    If you get an error than it sends an email  or gets added to the queue
    also have Rotating logs - logrotate - so one log file doesn't build up too much
    """