import sys
sys.path.append('H:\Python-webUI-auto')
import unittest
import HTMLTestRunner
import os
from testsuites.test_luntan import Luntan
from testsuites.test_luntan2 import Luntan2
from testsuites.test_luntan3 import Luntan3
from testsuites.test_luntan4 import Luntan4

cur_path=os.path.dirname(os.path.abspath("."))+"/report"
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Luntan))
suite.addTest(unittest.makeSuite(Luntan2))
suite.addTest(unittest.makeSuite(Luntan3))
suite.addTest(unittest.makeSuite(Luntan4))

if __name__=="__main__":
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner= HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="Dizcuz测试报告", description="关于lunt的测试报告")
    runner.run(suite)
