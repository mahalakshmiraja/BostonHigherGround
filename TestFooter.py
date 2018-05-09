import unittest
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestFooter(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def testfblink(self):
        """Launch the web page"""
        self.browser.get('https://higherground-boston.org/')
    
        """Click the facebook icon in the footer"""
        fbXpath = "/html/body/div[1]/footer/div[1]/div/div/div/div[3]/div/div[2]/div/div/span/a/i"
        Element= WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(fbXpath))
        Element.click()

      
if __name__ == '__main__':
    unittest.main()