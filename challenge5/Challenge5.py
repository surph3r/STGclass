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
        Cls_search = TNS
        Cls_search.run_search_copart(self, "porsche")

        select_qty = Select(self.driver.find_element(By.NAME, "serverSideDataTable_length"))
        select_qty.select_by_visible_text('100')
        wde_rows = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr')

        while True:
            wde_rows = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr')
            if len(wde_rows) == 100:
                break

        d_model_counts = {}
        d_damage_types = {
            'REAR END': 0,
            'FRONT END': 0,
            'MINOR DENT/SCRATCHES': 0,
            'UNDERCARRIAGE': 0,
            'MISC': 0
        }

        for i in range(len(wde_rows)):
            s_model_path = '//*[@id="serverSideDataTable"]/tbody/tr[' + str(i+1) + ']/td[6]'
            wde_model = self.driver.find_element(By.XPATH, s_model_path)
            if wde_model.text not in d_model_counts.keys():
                d_model_counts[wde_model.text] = 1
            else:
                d_model_counts[wde_model.text] += 1

            s_damage_path = '//*[@id="serverSideDataTable"]/tbody/tr[' + str(i + 1) + ']/td[12]'
            wde_damage = self.driver.find_element(By.XPATH, s_damage_path)
            if wde_damage.text in d_damage_types.keys():
                d_damage_types[wde_damage.text] += 1
            else:
                d_damage_types["MISC"] += 1

        if sum(d_model_counts.values()) == len(wde_rows) and sum(d_damage_types.values()) == len(wde_rows):
            print("Number of models = " + str(len(d_model_counts.keys())))
            print(d_model_counts)
            print("Types of damage")
            print(d_damage_types)
        else:
            print('You have failed this Challenge!')


if __name__ == '__main__':
    unittest.main()
