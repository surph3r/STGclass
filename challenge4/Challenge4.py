import unittest
from num2words import num2words
from fibonacci import *


class Challenge4(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        # self.driver = webdriver.Chrome("../chromedriver.exe")
        pass

    def tearDown(self):
        # code to close webdriver
        # self.driver.close()
        pass

    def test_challenge4(self):
        # code for our test steps
        my_num = 21
        my_ord_num = num2words(my_num, ordinal=True)
        my_ord_num = my_ord_num.replace('-', ' ')

        fib_num = fibonacci(my_num)
        word_salad = num2words(fib_num)
        word_salad = word_salad.replace('-', ' ')

        print('The ' + my_ord_num + ' Fibonacci number is: ' + str(fib_num) + ' - ' + word_salad)


if __name__ == '__main__':
    unittest.main()
