from testsuites.base_testcase import BaseTestCase
from pageobjects.luntan_homepage import HomePage
import unittest
import time
class Luntan3(BaseTestCase):
    def test_example3(self):
        home_page=HomePage(self.driver)
        home_page.login("zyx521","zyx19980315")
        home_page.search_tiezi("haotest")
        # home_page.assert_haotest()
        time.sleep(5)
        home_page.login_out()

if __name__=="__main__":
    unittest.main()