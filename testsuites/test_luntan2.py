from testsuites.base_testcase import BaseTestCase
from pageobjects.luntan_homepage import HomePage
import unittest
import time
class Luntan2(BaseTestCase):
    def test_example2(self):
        home_page=HomePage(self.driver)
        home_page.login_byadmin('admin','admin')
        home_page.delete_tie()
        home_page.manege_guanli()
        home_page.add_new_bankuai("987")
        home_page.login_out()
        time.sleep(5)
        home_page.login('zyx521','zyx19980315')
        home_page.write_new_tie("987","nyx5211314521")
        home_page.huifu("你是啥子嘛？三十多吃豆腐")


if __name__=="__main__":
    unittest.main()