from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from selenium import webdriver
import time
import os.path
logger=Logger(logger='BasePage').getlog()
# import unittest
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")
    def open_url(self,url):
        self.driver.get(url)

    def quite_browser(self):
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
            logger.info("Close and quit the browser.")
        except Exception as e:
            logger.error("Failed to quit the browser with %s"%e)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logger.error("%s页面元素未找到%s"%(self, loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            logger.error("%s页面元素未找到%s" % (self, loc))

    def sendkeys(self, text, *loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("%s 被输入" %text)
        except Exception as e:
            logger.error("Failed to type in input box with %s"%text)
            self.get_windows_img()

    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("成功点击")
        except:
            logger.error("Failed to be clicked")

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path + rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshort and save to folder: /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshort! %s"%e)

    def avtive_current_windows(self,i):
        self.driver.switch_to.window(self.driver.window_handles[i])

    def avtive_current_windows1(self,j):
        self.driver.switch_to.frame(j)

    def get_text(self,*loc):
        el = self.find_element(*loc)
        return el.text

    def move_to_element(self,i,*loc):
        el = self.find_element(*loc)
        try:
            el.move_to_element(self.driver.find_element_by_css_selector(i)).perform()
            logger.info("鼠标悬停")
        except:
            logger.error("Failed to 鼠标悬停")


    def assert_equal(self,unittest,first,second,msg):
        try:
            unittest.assertEqual(first,second,msg)
        finally:
            self.get_windows_img()
            time.sleep(5)

    def get_ratios(self,*loc):
        e1=self.find_elements(*loc)
        ratio_list=[]
        choice_list=[]
        for i in range(0,len(e1)-1):
            if i%2!=0:
                ratio_list.append(e1[i].text)
            else:
                choice_list.append(e1[i].text)
        return ratio_list,choice_list




    def find_text(self,*loc):
        el = self.find_element(*loc)
        text=el.text
        return text

