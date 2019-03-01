from testsuites.base_testcase import BaseTestCase
from pageobjects.luntan_homepage import HomePage
import unittest
import time
class Luntan4(BaseTestCase):
    def test_example4(self):
        home_page=HomePage(self.driver)
        home_page.login("zyx521","zyx19980315")
        home_page.write_a_tie()
        home_page.toupiao()
        home_page.write_piao("what's your favorite game","cf",'lol','dnf','game111111111111111111111111111')
        home_page.choise()
        print(home_page.result_1())
        time.sleep(5)


if __name__=="__main__":
    unittest.main()