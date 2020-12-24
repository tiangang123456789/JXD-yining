import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""
* 文件名：  Fuyong.py
* 描述：    代码复用率高，修改幅度比较小
* 创建人：  郭威
* 创建时间：2020-12-21
"""

#保存
def Save_Info(driver):
    js_Save_Info = 'document.querySelector("#add").click()'
    driver.execute_script(js_Save_Info)

#关闭
def Cloose_Info(driver):
    js_Cloose_Info = 'document.querySelector("#cancel").click()'
    driver.execute_script(js_Cloose_Info)

#用户名
def UserName(driver, usrname):
    # 输入用户名
    driver.find_element_by_name("username").send_keys(usrname)

#密码
def Pwd(driver, pwd):
    # 输入密码
    driver.find_element_by_name("cipher").send_keys(pwd)

# 进入伊宁系统
def Sys_tem(driver):
    driver.find_element_by_id("login").click()

#鼠标右键操作
def MiGi_Click(driver, migi):
    ActionChains(driver).context_click(migi).perform()

#鼠标双击操作
def Double2_Click(driver, double2):
    ActionChains(driver).double_click(double2).perform()

#键盘 PAGE_DOWN 按键
def PgDn(driver,pgdn_key):
    ActionChains(driver).key_down(Keys.PAGE_DOWN, pgdn_key).perform()

#键盘 TAB 按键
def Tab_Key(driver, tab_key):
    ActionChains(driver).key_down(Keys.TAB, tab_key).key_up(Keys.TAB).perform()

#粘贴板信息
def ZhanTieban(driver):
    driver.find_element_by_xpath('//*[@id="mouse-menu"]/li[6]').click()
    time.sleep(0.5)
    for num in range(1,13):
        info = str(num)+'粘贴板信息'
        if num < 12:
            driver.find_element_by_xpath('//*[@id="pasteData"]').send_keys(info+'\n')
        else:
            driver.find_element_by_xpath('//*[@id="pasteData"]').send_keys(info)
    '''
    driver.find_element_by_xpath('//*[@id="pasteData"]').send_keys(
        '1粘贴板信息\n\
         2粘贴板信息\n\
         3粘贴板信息\n\
         4粘贴板信息\n\
         5粘贴板信息\n\
         6粘贴板信息\n\
         7粘贴板信息\n\
         8粘贴板信息\n\
         9粘贴板信息\n\
         10粘贴板信息\n\
         11粘贴板信息\n\
         12粘贴板信息\n\
         13粘贴板信息')
     '''
#计划开始时间--计划结束时间
def Plan_start_end(driver):
    Plan_start(driver)
    time.sleep(0.5)
    Plan_end(driver)

def Plan_start(driver):
    #计划开始时间
    #点击计划开始时间
    driver.find_element_by_xpath(
        '//*[@id="planStartTime"]').click()
    time.sleep(0.5)
    #选择想要的时间（年月日）
    driver.find_element_by_xpath(
        '//*[@id="layui-laydate2"]/div[1]/div[2]/table/tbody/tr[1]/td[1]').click()
    time.sleep(0.5)
    
    #点击确定
    driver.find_element_by_xpath(
        '//*[@id="layui-laydate2"]/div[2]/div/span[2]').click()
    
def Plan_end(driver):
    #计划结束时间
    #点击计划结束时间
    driver.find_element_by_xpath(
        '//*[@id="planEndTime"]').click()
    time.sleep(0.5)
    #选择想要的时间（年月日）
    driver.find_element_by_xpath(
        '//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[6]/td[7]').click()
    time.sleep(0.5)
    #点击确定
    driver.find_element_by_xpath(
        '//*[@id="layui-laydate1"]/div[2]/div/span[2]').click()
