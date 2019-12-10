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

    def test_challenge3(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        # Let's pause for station identification
        WebDriverWait(self.driver, 1)

        popularSearches = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[1]/div[2]//a')
        numSearches = len(popularSearches)

        print("FOR Loop iteration:")
        for item in range(numSearches):
            print(popularSearches[item].text + " - " + popularSearches[item].get_attribute('href'))

        print("\n" + "WHILE Loop iteration:")
        i = 0
        while i < numSearches:
            if i == 20:
                break
            print(popularSearches[i].text + " - " + popularSearches[i].get_attribute('href'))
            i+=1


if __name__ == '__main__':
    unittest.main()
