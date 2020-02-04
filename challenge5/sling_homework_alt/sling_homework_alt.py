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
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located) # give it a sec for stuff to load

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_sling_for_alt_tags(self):
        wde_elements = self.driver.find_elements(By.XPATH, '/html/body//*')
        i_num_elements = len(wde_elements)
        print('Number of page elements = ' + str(i_num_elements))

        for e in wde_elements:
            print(e.get_attribute('alt'))
            print(e.get_property('localName'))


if __name__ == '__main__':
    unittest.main()
