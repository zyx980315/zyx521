from testsuites.base_testcase import BaseTestCase
from pageobjects.luntan_homepage import HomePage
import unittest
import time
class Luntan(BaseTestCase):
    def test_example1(self):
        home_page=HomePage(self.driver)
        home_page.login('zyx521','zyx19980315')
        home_page.search('张彦鑫',"我爱nyx，爱他的美，然后没了")

        home_page.huifu("12356478996")
        time.sleep(5)
        home_page.login_out()
if __name__=="__main__":
    unittest.main()