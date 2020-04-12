import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# created logger if you do mot configure this it will get format from root logger
file_handler = logging.FileHandler('employee2logger.log')     # created file handler

#  created file handler at line 5 and should add this to file handler not to logger
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)                         # added this file handler to logger


# logging.basicConfig(filename='employee2.log', level=logging.INFO,
#                     format='%(levelname)s:%(name)s:%(message)s')

class Employee:
    """ A sample Employee class """

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))


    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
