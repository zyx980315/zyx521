from testsuites.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage
import unittest
import time
class BaiduSearch(BaseTestCase):
    def test_baidu_seach(self):
        home_page=HomePage(self.driver)
        home_page.search('百度两下')
        time.sleep(5)

if __name__=="__main__":
    unittest.main()