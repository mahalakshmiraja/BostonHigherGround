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
        """Check the navigation to families pages"""
        whatwedo="//*[@id='menu-item-140']/div/a"
        WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(whatwedo)).click()
        forfamilies = "//*[@id='menu-item-136']/a"
        WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(forfamilies)).click()
        """Check moreinfo link"""
        moreInfo="//*[@id='fl-post-132']/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/h4/em/a"
        WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(moreInfo)).click()
        """Redirect to ContactUs page"""
        ContactUs = WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='fl-post-21']/div/div[1]/div/div/div/div/div/div/div[3]/div/div/h2/strong")) 
        if ContactUs.is_displayed():
            print("Test Passed")
        else:
            print("Error! Try Again")

if __name__ == '__main__':
    unittest.main()