import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class Challenge1(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge1(self):
        # code for our test steps
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
