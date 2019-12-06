import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge3_forloop(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        WebDriverWait(self.driver,1)
        popularSearches = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[1]//a')
        popularSearches[0].get_attribute()
        print(popularSearches)
        # getThirdListItem.get_attribute(self.driver,"a")

    def test_challenge3_whileloop(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        WebDriverWait(self.driver,1)
        popularSearches = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[1]//a')
        while(i++):
            if popularSearches[i]:
                pass
            else:
                break
        # getThirdListItem.get_attribute(self.driver,"a")


if __name__ == '__main__':
    unittest.main()
