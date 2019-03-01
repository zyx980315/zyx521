from selenium.webdriver.common.by import By
from framework.base import BasePage
from selenium import webdriver
import time
import unittest
class HomePage(BasePage):
    # 登录
    login_button=(By.XPATH,"//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button/em")
    user=(By.NAME,"username")
    psd=(By.NAME,"password")
    moren = (By.CSS_SELECTOR,'.fl_tb h2 a')
    #发帖
    title=(By.ID,'subject')
    zhengwen = (By.ID, 'fastpostmessage')
    fatie=(By.CSS_SELECTOR,'.ptm .pn strong')
    #回复
    huitie=(By.ID,"fastpostmessage")
    huitie_button=(By.ID,'fastpostsubmit')
    #退出
    login_out_button=(By.LINK_TEXT,'退出')
    # 删帖
    delete=(By.NAME,'moderate[]')
    shanchu=(By.LINK_TEXT,'删除')
    yes=(By.XPATH,'//*[@id="modsubmit"]/span')
    #管理中心  论坛
    manege_center=(By.LINK_TEXT,'管理中心')
    luntan=(By.LINK_TEXT,"论坛")
    #创建新的板块
    add=(By.CSS_SELECTOR,'.addtr')
    new_name=(By.NAME,"newforum[1][]")
    post=(By.XPATH,'//*[@id="submit_editsubmit"]')
    #发新贴
    new_tie=(By.CSS_SELECTOR,'table tbody .fl_row:nth-last-child(2) h2 a')
    bankuai=(By.XPATH,'//*[@id="pt"]/div/a[2]')
    #搜索haotest
    search_a=(By.NAME,'srchtxt')
    sousuo=(By.ID,'scbar_btn')
    searcH=(By.XPATH,'//*[@id="30"]/h3/a/strong/font')
    #投票
    button_fatie=(By.XPATH,'//*[@id="newspecial"]/img')
    button_toupiao=(By.XPATH,'//*[@id="newspecial_menu"]/li[2]/a')
    title_toupiao=(By.ID,'subject')
    choise1 = (By.CSS_SELECTOR, ".mbm .px")
    choise2 = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    choise3 = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")
    zw=(By.XPATH,'/html/body')
    button_toupiao_anniu=(By.XPATH,'//*[@id="postsubmit"]/span')

    #投票
    choise4=(By.NAME,'pollanswers[]')
    butt=(By.XPATH,'//*[@id="pollsubmit"]/span')
    #取主题
    take=(By.XPATH,'//*[@id="thread_subject"]')
    asd=(By.XPATH,'//*[@id="visitedforums"]/a')

    #结果统计
    result=(By.CSS_SELECTOR,'.pcht tr')
    zhuti=(By.ID,'thread_subject')
    def login(self,a,b):
        self.sendkeys(a, *self.user)
        self.sendkeys(b, *self.psd)
        self.click(*self.login_button)
    def search(self,c,d):
        time.sleep(3)
        self.click(*self.moren)
        self.sendkeys(c,*self.title)
        self.sendkeys(d,*self.zhengwen)
        self.get_windows_img()
        self.click(*self.fatie)
    def huifu(self,j):
        self.sendkeys(j,*self.huitie)
        self.click(*self.huitie_button)
    def login_out(self):
        self.avtive_current_windows(0)
        self.click(*self.login_out_button)
        time.sleep(3)

    def login_byadmin(self,a,b):
        self.sendkeys(a, *self.user)
        self.sendkeys(b, *self.psd)
        self.click(*self.login_button)
    def delete_tie(self):
        time.sleep(3)
        self.click(*self.moren)
        self.click(*self.delete)
        self.click(*self.shanchu)
        self.click(*self.yes)
    def manege_guanli(self):
        self.click(*self.manege_center)
        self.avtive_current_windows(1)
        self.click(*self.luntan)
    def add_new_bankuai(self,o):
        self.avtive_current_windows1(0)
        self.click(*self.add)
        self.sendkeys(o,*self.new_name)
        self.click(*self.post)
        time.sleep(3)

    def write_new_tie(self,x,y):
        time.sleep(3)
        self.click(*self.bankuai)
        time.sleep(5)
        self.click(*self.new_tie)
        time.sleep(5)
        self.sendkeys(x, *self.title)
        self.sendkeys(y, *self.zhengwen)
        time.sleep(5)
        self.click(*self.fatie)

    def search_tiezi(self,g):
        self.sendkeys(g,*self.search_a)
        time.sleep(2)
        self.click(*self.sousuo)
        time.sleep(5)
        self.avtive_current_windows(1)
    def assert_haotest(self):
        first=self.find_text(*self.searcH)
        self.assert_equal(unittest,first,"haotest","msg")

    def write_a_tie(self):
        time.sleep(3)
        self.click(*self.bankuai)

    def toupiao(self):
        self.click(*self.new_tie)
        time.sleep(5)
        self.move_to_element('.bm a img',*self.fatie)
        time.sleep(5)
        self.click(*self.button_toupiao)
        time.sleep(10)

    def write_piao(self,q,w,u,i,r):
        self.sendkeys(q,*self.title_toupiao)
        self.sendkeys(w,*self.choise1)
        self.sendkeys(u, *self.choise2)
        self.sendkeys(i, *self.choise3)
        time.sleep(5)
        self.avtive_current_windows1(0)
        self.sendkeys(r,*self.zw)
        self.avtive_current_windows(0)
        time.sleep(3)
        self.click(*self.button_toupiao_anniu)
        time.sleep(3)
        self.get_text(*self.take)
        time.sleep(5)

    def choise(self):
        self.click(*self.choise4)
        time.sleep(5)
        self.click(*self.butt)
        time.sleep(5)

    def result_1(self):
        print("投票的内容以及情况：",self.get_ratios(*self.result))
        print("投票主题是：",self.get_text(*self.zhuti))