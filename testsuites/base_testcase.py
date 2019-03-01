from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.Browser=BrowserEngine()
        self.driver=self.Browser.open_browser()
        # self.driver.implicitly_wait(5)

    def tearDown(self):
        print("测试结束")
        # self.driver.quit()
        self.driver = self.Browser.quit_browser()