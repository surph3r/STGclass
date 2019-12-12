import unittest
from libMyFunctions import fibonacci_sequence as fib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
        my_num = fib(9)
        print('The 9th order Fib Seq is: ' + str(my_num))


if __name__ == '__main__':
    unittest.main()
