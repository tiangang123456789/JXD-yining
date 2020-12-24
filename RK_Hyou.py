import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC

import SinKi
import Fuyong
"""
* 文件名：  RK_Hyou.py
* 描述：    热控工作票新建内容填写
* 创建人：  郭威
* 创建时间：2020-12-21
"""

#热控工作票
def RK_Piao(driver):
    driver.implicitly_wait(5)
  
    #工作班成员
    SinKi.SaGyou_ChengYuan(driver)
    time.sleep(0.3)
    #工作任务:
    driver.find_element_by_xpath(
        "//*[@id='worktask']").send_keys(
            "伊宁市智慧能源有限公司热控工作票工作内容!")
    time.sleep(0.1)
    #序号1
    SinKi.SaGyou_NaiYou(driver)
    time.sleep(0.5)
    #下一页
    """
    driver.current_window_handle   #切换窗口
    driver.switch_to.default_content()
    driver.switch_to.frame(
    driver.find_element_by_xpath(
        "//iframe[starts-with(@tab-id, '2')]"))
    """
    JS_Page = driver.find_element_by_xpath(
        '//*[@id="worktask"]')
    Fuyong.PgDn(driver, JS_Page)
    time.sleep(0.5)
    #计划开始时间--计划结束时间
    Fuyong.Plan_start_end(driver)
    time.sleep(0.5)
    #需要退出热工保护或自动装置名称：
    driver.find_element_by_xpath(
        '//*[@id="equipName"]').send_keys(
            '需要退出热工保护或自动装置名称')
    time.sleep(0.5)
    #6.1 由运行人员执行的安全措施：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable1"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_61 = 'document.querySelector("#layui-layer2 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_61)
    time.sleep(0.5)
    JS_Page1 = driver.find_element_by_xpath(
        '//*[@id="all"]/div[2]/table/tbody/tr[9]/td')
    #键盘 PAGE_DOWN 按键
    Fuyong.PgDn(driver, JS_Page1)
    time.sleep(0.5)
    #6.3 由工作负责人执行的安全措施：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable3"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_63 = 'document.querySelector("#layui-layer3 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_63)
    time.sleep(0.5)
 
    
    #保存到草稿箱
    Fuyong.Save_Info(driver)
    time.sleep(2)
    #关闭
    Fuyong.Cloose_Info(driver)
    #time.sleep(3) # 暂停300秒
    #driver.close()
    '''
    driver.find_element_by_xpath(
        '//*[@id="establishOperation"]').click()
    time.sleep(5)
    
    #driver.switch_to_alert
    #wait.until(EC.alert_is_present())
    #driver.switch_to.alert.accept()
    #js = 'document.querySelector("#layui-layer2 > div.layui-layer-title").click()'
    #driver.execute_script(js)
    #driver.find_element_by_xpath(
    #    '//*[@onclick="TwHeatcontrolWorkticketInfoDlg.addsave()"]').click()
    
    #driver.switch_to_default_content()
    driver.switch_to.frame(
    driver.find_element_by_xpath(
        "//iframe[starts-with(@id, 'layui-layer-iframe4')]"))
    
    driver.find_element_by_xpath('*[onclick="TwSafetyRiskControlInfoDlg.addsave()"]').click()
    #webdriver.ActionChains(driver).move_to_element(aa).click(aa).perform()
    #js1 = 'document.querySelector("#add").click()'
    #driver.execute_script(js1)
    
    time.sleep(111)
    '''


    
