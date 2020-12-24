import Login
import SinKi
import RK_Hyou
import RJ_Hyou
import HP_Hyou
import time

"""
* 文件名：  Hyou.py
* 描述：    新建工作票：工作票--开票
* 创建人：  郭威
* 创建时间：2020-12-19
* 修改人：
* 修改时间：
* 修改内容：。。。。。。
"""

#创建工作票
"""
 hyou_number=1,热控工作票票；
 hyou_number=2,热力机械工作票；
 hyou_number=3,三合一工作票；
"""
def Hard_List(driver, hyou_number, jizu_number, zhuanye_number):
    #隐示等待,用于异常情况
    driver.implicitly_wait(5)
    # 输入用户名密码
    Login.Users_Pwd(driver, hyou_number)
    time.sleep(1)
    #工作票--开票
    SinKi_Hyou(driver, hyou_number, jizu_number, zhuanye_number)
    time.sleep(1.5)
    if hyou_number == 1:
        RK_Hyou.RK_Piao(driver)
    elif hyou_number == 2:
        RJ_Hyou.RJ_Piao(driver)
    elif hyou_number == 3:
        HP_Hyou.HP_Piao(driver)
        


'''
共通：きょうつう
进入系统后，新建工作票
1.左侧选择：工作票--新建工作票
2.新建工作票：选择票类型--机组--专业--工作内容--开票
'''
"""
    hyou_number=1,热控工作票票；
    hyou_number=2,热力机械工作票；
    hyou_number=3,三合一工作票；
"""
def SinKi_Hyou(driver, hyou_number, jizu_number, zhuanye_number):
    driver.find_element_by_xpath(
        "//a[@title='工作票']").click()
    driver.find_element_by_xpath(
        "//a[@title='新建工作票']").click()
    time.sleep(1)
    #定位到右侧面板
    SinKi.Migi_Div(driver)
    time.sleep(0.3)
    #票类型(选择工作票类型)
    driver.find_element_by_xpath(
         '//*[@id="div_ticketType"]/div[2]/div/div/div/input').click()
    time.sleep(0.3)
    SinKi.Hyou_type(driver, hyou_number)
    time.sleep(0.3)
    #机组
    driver.find_element_by_xpath(
        '//*[@id="div_crew"]/div[2]/div/div/div/input').click()
    time.sleep(0.3)
    SinKi.JiZu_name(driver, jizu_number)
    time.sleep(0.3)
    #专业
    driver.find_element_by_xpath(
        "//*[@id='div_workapprivaldeptname']/div[2]/div/div/div/input").click()
    time.sleep(0.3)
    SinKi.ZhuanYe_name(driver, zhuanye_number)
    time.sleep(0.3)
    #(开票前需要填写的)工作内容
    SinKi.KaiPiao_naiyou(driver, hyou_number)
    time.sleep(0.3)
    #开票
    driver.find_element_by_xpath(
        "//*[@id='submit']").click()
    
 



