import time
from selenium.webdriver.support.ui import Select

import SinKi
import Fuyong
"""
* 文件名：  Work_list.py
* 描述：    仓库管理
* 创建人：  郭威
* 创建时间：2020-12-23
* 修改人：
* 修改时间：
* 修改内容：。。。。。。
"""

#工作票列表

def Work_list(driver)
#隐示等待,用于异常情况
    driver.implicitly_wait(5)
    # 输入用户名密码  默认任意用户
    Login.Users_Pwd(driver, 1)
    time.sleep(1)
    
    driver.find_element_by_xpath(
        "//a[@title='仓储管理']").click()
    time.sleep(0.1)
    driver.find_element_by_xpath(
        "//a[@title='盘盈单']").click()
    time.sleep(0.1)
    driver.find_element_by_xpath(
        "//a[@title='盘盈单待办']").click()
    time.sleep(1)
    #定位到右侧面板
    def Migi_Div(driver):
    driver.switch_to.frame(
    driver.find_element_by_xpath(
        "//iframe[starts-with(@tab-id, '77')]"))
    time.sleep(0.3)
