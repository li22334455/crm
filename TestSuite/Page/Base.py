#Base层在项目中涉及底层操作，如click,send_keys及clear等等
from selenium import webdriver
#我们日常操作页面的一些动作
from selenium.webdriver.common.by import By

class base():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver=webdriver.Chrome(chrome_options=options)
    def __init__(self):#初始化
        self.driver.get("https://www.ctrip.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # 查找元素的方法
        # *此时这个*代表可以接收任意多个非关键字参数
        # 查找元素
    def find(self,*args):
        try:
            return self.driver.find_element(*args)
        except:
            print("定位失败")
    #这是点击动作的方法
    aargsid = By.ID
    def click(self,*args):
        self.find(*args).click()
    #这是一个清除的方法
    def clear(self,*args):
        self.find(*args).clear()
    #输入的方法
    def sendkey(self,*args,value):
        self.find(*args).send_keys(value)
    #操作滚动条
    def js(self,str):
        self.driver.execute_script(str)
    #获取URL的方法
    def url(self):
        return self.driver.current_url
    #后退的回退
    def back(self):
        self.driver.back()
    #前进的方法
    def forword(self):
        self.driver.forward()
    #关闭的浏览器与驱动的方法
    def quit(self):
        self.driver.quit()
