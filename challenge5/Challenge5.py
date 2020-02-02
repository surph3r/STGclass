import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.TopNavSearch import TopNavSearch as TNS


class Challenge5(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        WebDriverWait(self.driver, 1)  # give it a sec for stuff to load

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge5(self):
        TNS.run_search_copart(self, "porsche")

        select_qty = Select(self.driver.find_element(By.NAME, "serverSideDataTable_length"))
        select_qty.select_by_visible_text('100')
        rows = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr')

        while True:
            rows = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr')
            if len(rows) == 100:
                break

        model_counts = {}
        for i in range(len(rows)):
            model_path = '//*[@id="serverSideDataTable"]/tbody/tr[' + str(i+1) + ']/td[6]'
            element = self.driver.find_element(By.XPATH, model_path)
            if element.text not in model_counts.keys():
                model_counts[element.text] = 1
            else:
                model_counts[element.text] += 1

        if sum(model_counts.values()) == len(rows):
            print("Number of models = " + str(len(model_counts.keys())))
            print(model_counts)
        else:
            print('You have failed this Challenge!')


if __name__ == '__main__':
    unittest.main()
