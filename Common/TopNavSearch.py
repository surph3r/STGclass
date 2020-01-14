from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TopNavSearch:
    def __init__(self, driver):
        self.driver = driver


    def run_search(selfself, query):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        searchField = self.driver.find_element(By.ID, "input-search")
        searchField.clear()
        searchField.click()
        # searchField.send_keys("exotics")
        searchField.send_keys(Keys.ENTER)
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
