import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge2(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        searchField = self.driver.find_element(By.ID, "input-search")
        searchField.clear()
        searchField.click()
        searchField.send_keys("exotics")
        searchField.send_keys(Keys.ENTER)
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
        self.assertIn("PORSCHE", self.driver.page_source)


if __name__ == '__main__':
    unittest.main()
