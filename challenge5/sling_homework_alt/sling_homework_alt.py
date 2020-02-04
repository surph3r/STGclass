import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge5Bonus(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        self.driver = webdriver.Chrome("../../chromedriver.exe")
        self.driver.get("https://www.sling.com")
        self.assertIn("Sling TV", self.driver.title)
        WebDriverWait(self.driver, 1) # give it a sec for stuff to load

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_sling_for_alt_tags(self):
        wde_elements = self.driver.find_elements(By.XPATH, '//*')
        print('Number of page elements = ' + str(len(wde_elements)))

        for e in wde_elements:
            print(e.get_attribute('alt'))


if __name__ == '__main__':
    unittest.main()
