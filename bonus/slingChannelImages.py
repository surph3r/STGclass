###
# Go to Sling.com site. Grab all the channel logos for Orange.
# Print the Alt text channel name and logo source href
###

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge3SlingChannelImages(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.sling.com")
        self.assertIn("Sling TV", self.driver.title)
        WebDriverWait(self.driver, 1)  # give it a sec for stuff to load

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_channel_images(self):
        pics = self.driver.find_elements(By.XPATH, '//*[@id="channelList"]//img')
        count = len(pics)
        print("Image count = " + str(count))

        i = 0
        while i < count:
            print(pics[i].get_attribute("alt") + " - " + pics[i].get_attribute('src'))
            i+=1


if __name__ == '__main__':
    unittest.main()
