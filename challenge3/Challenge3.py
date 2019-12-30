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
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        WebDriverWait(self.driver, 1) # give it a sec for stuff to load

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge3_for_loop(self):
        popularSearches = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[1]/div[2]//a')
        numSearches = len(popularSearches)

        print("My version of the FOR Loop iteration:")
        for item in range(numSearches):
            print(popularSearches[item].text + " - " + popularSearches[item].get_attribute('href'))

        print("\n" + "Teacher's version of the FOR Loop:")
        elements = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[1]//a')
        for count in elements:
            print(count.text + ': ' + count.get_attribute("href"))

    def test_challenge3_while_loop(self):
        categories = self.driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]/../div[3]//a')
        numSearches = len(categories)

        print("\n" + "WHILE Loop iteration:")
        i = 0
        while i < numSearches:
            print(categories[i].text + " - " + categories[i].get_attribute('href'))
            i+=1


if __name__ == '__main__':
    unittest.main()
