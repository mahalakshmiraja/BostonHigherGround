import unittest
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestFooter(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def testmapslink(self):
        """Launch the web page"""
        self.browser.get('https://higherground-boston.org/')
    
        """Click the directions icon in the footer"""
        gotosDirectionsXpath = "/html/body/div[1]/footer/div[1]/div/div/div/div[4]/div/div[2]/div/div/span/a/i"
        gotoDirectionElement= WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(gotosDirectionsXpath))
        gotoDirectionElement.click()

        
if __name__ == '__main__':
    unittest.main()