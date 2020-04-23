import unittest
from employee import Employee           # importing Employee class from employee module
from unittest.mock import patch         # can use patch as a decorator or as a context manager


class TestEmployee(unittest.TestCase):        # inherits from unittest.TestCase

    @classmethod
    def setUpClass(cls):
        print('setupClass')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    """ these are classmethods means that we are working with class rather than the instance of the class
        works once before and after anything.
        For example: we may want to populate a database to run tests against, as long as we are just reading
        from the database then it might appropriate to just set this up once in the setUp class method 
        and then we can tear it down in the tearDown class method  """


    """ dry = don't repeat yourself """
    def setUp(self):                          # will run up before every single test
        print('setUp')
        self.emp1 = Employee('Corey', 'Schafer', 50000)
        self.emp2 = Employee('Sue', 'Smith', 60000)
        """ in order to access those from within our other tests we're actually going to have to 
            set these as instance attributes by putting 'self.emp1' and 'self.emp2' """
    def tearDown(self):                       # will run after every single test
        # pass
        print('tearDown\n')
        """ use case: for example: 
            we had some functions to test that added files to a directory or to a database 
            then in setUp method --> create the test directory or the test database to hold those files
            and in the tearDown method --> we could delete all of those so that we have a clean slate for next test """

    def test_email(self):
        print('test_email')
        # emp1 = Employee('Corey', 'Schafer', 50000)
        # emp2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')

        self.emp1.first = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        # emp1 = Employee('Corey', 'Schafer', 50000)
        # emp2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp2.fullname, 'Sue Smith')

        self.emp1.first = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.fullname, 'John Schafer')
        self.assertEqual(self.emp2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        # emp1 = Employee('Corey', 'Schafer', 50000)
        # emp2 = Employee('Sue', 'Smith', 60000)

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            """ test failed response too """

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

    # def test_something(self):
    #     self.assertEqual(True, False)

""" Tests don't necessarily run in order
    thats why we need to keep all of our tests isolated from one another """


if __name__ == '__main__':
    unittest.main()
