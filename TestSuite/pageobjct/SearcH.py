from TestSuite.Page.Base import base
from selenium.webdriver.common.by import By
import time
import pyautogui

# def find(self, *args):
#     try:
#         return self.driver.find_element(*args)
#     except:
#         print("定位失败")
class Searchpage(base):
    #找到“火车”位置
    def search(self):
        return self.find(By.XPATH,"/html/body/div[9]/div/ul/li[6]/b")
     #找到”往返“位置
    def search1(self):
        return self.find(By.ID,"roundTrip")
     #找到”起点“位置
    def search2(self):
        return self.find(By.ID,"notice01")
     #找到出发日期位置
    def search3(self):
        return self.find(By.ID,"DdateObj")
     #找到到达
    def search4(self):
        return self.find(By.ID,"notice02")
     #找到返程日期
    def search5(self):
        return self.find(By.ID,"AdateObj")
     #找到搜索按纽
    def search6(self):
        return self.find(By.ID,"searchTicket")

    #编写测试用例
    def search7(self,leave,leave_data,arrive,arrive_data):
        time.sleep(10)
        #点击火车
        self.search().click()
        #往返
        self.search1().click()
        #输入起点位置
        self.search2().send_keys(leave)
        time.sleep(2)
        #输入出发发时间
        self.search3().send_keys(leave_data)
        time.sleep(2)
        #输入终点站
        self.search4().send_keys(arrive)
        time.sleep(2)
        #输入到达时间
        self.search5().send_keys(arrive_data)
        time.sleep(2)
        #输入返程日期后点击空白处，让日期框消失
        pyautogui.moveTo(359, 551)
        pyautogui.click()
        time.sleep(2)
        #点击搜索
        self.search6().click()
# # username_1=(By.ID,"idinput")
# base.click(username_1)