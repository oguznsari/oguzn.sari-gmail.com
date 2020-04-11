import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,          # Employee creation is good example for INFO
    format='%(asctime)s:%(levelname)s:%(message)s ')

class Employee:
    """ A sample employee class """

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print('Created Employee: {} - {}'.format(self.fullname, self.email))
        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')


""" good start for now but, there are some issues that we can run into once we start importing our other modules
    because they are all try to share the same logger 
    - create seperate logger
    - add handlers and formatters to those loggers
    - how we can log our information to multiple locations """