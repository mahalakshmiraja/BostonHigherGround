import unittest
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestFooter(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def testfamiliespage(self):
        """Launch the web page"""
        self.browser.get('https://higherground-boston.org/')
        """Check the navigation to partners pages"""
        whatwedo="//*[@id='menu-item-140']/div/a"
        WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(whatwedo)).click()
        ForPartners = "//*[@id='menu-item-135']/a"
        WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(ForPartners)).click()
        """Check JoinUs feature"""
        JoinUs="//*[@id='fl-post-129']/div/div[1]/div/div/div/div[2]/div/div/div/div/div/a/span"
        WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(JoinUs)).click()
        ContactUs = WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='fl-post-21']/div/div[1]/div/div/div/div/div/div/div[3]/div/div/h2/strong")) 
        if ContactUs.is_displayed():
            print("Test Passed")
        else:
            print("Error! Try Again")

if __name__ == '__main__':
    unittest.main()