###
# Go to Sling.com Help site. Do a search for Roku.
# Validate that search results exist
###

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge3SlingSearch(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://help.sling.com")
        self.assertIn("Help Center", self.driver.title)
        WebDriverWait(self.driver, 1) # give it a sec for stuff to load

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_sling_search(self):
        # code for our test steps
        searchTerm = "airtv"
        searchField = self.driver.find_element(By.ID, "support-search-input")
        searchField.clear()
        searchField.click()
        searchField.send_keys(searchTerm)
        btnSearch = self.driver.find_element_by_xpath('//*[@id="hc-search-form"]//button')
        btnSearch.click()

        try:
            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div[2]//a")))
        except:
            print("There are no search results")
        else:
            searchResults = self.driver.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]//a")
            print("Here are your " + searchTerm + " search results")
            for item in searchResults:
                print(item.text + ": " + item.get_attribute("href"))


if __name__ == '__main__':
    unittest.main()
