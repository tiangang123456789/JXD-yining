import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC

import SinKi
import Fuyong
"""
* 文件名：  HP_Hyou.py
* 描述：    热控工作票新建内容填写
* 创建人：  郭威
* 创建时间：2020-12-21
"""

#三合一工作票
def HP_Piao(driver):
    driver.implicitly_wait(5)
  
    #工作班成员
    SinKi.SaGyou_ChengYuan(driver)
    time.sleep(0.3)
    #工作任务:
    driver.find_element_by_xpath(
        "//*[@id='workTasks']").send_keys(
            "伊宁市智慧能源有限公司热控工作票工作内容!")
    time.sleep(0.1)
    #序号1
    #SinKi.SaGyou_NaiYou1(driver)
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
        '//*[@id="all"]/div[2]/table/tbody/tr[8]/td/div[1]/div[2]/div[1]/table/thead/tr/th[3]/div[1]')
    Fuyong.PgDn(driver, JS_Page)
    time.sleep(0.5)
    
    #计划开始时间--计划结束时间
    Fuyong.Plan_start_end(driver)
    time.sleep(0.5)
    #5.电气工作条件:
    driver.find_element_by_xpath(
        '//*[@id="all"]/div[2]/table/tbody/tr[10]/td/span[4]/input').click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        '//*[@id="allBlackouts"]').send_keys('任意填写')
    time.sleep(0.5)
    #6.运行必须采取的安全措施(按操作顺序填写并执行)
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
        
    #7.需检修自理的安全措施(按工作顺序填写并执行)
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable2"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_63 = 'document.querySelector("#layui-layer3 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_63)
    time.sleep(0.5)

    JS_Page1 = driver.find_element_by_xpath(
        '//*[@id="all"]/div[2]/table/tbody/tr[14]/td/div[1]/div[2]/div[1]/table/thead/tr/th[2]/div[1]')
    #键盘 PAGE_DOWN 按键
    Fuyong.PgDn(driver, JS_Page1)
    time.sleep(0.5)

    #8.安全注意事项
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable3"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_63 = 'document.querySelector("#layui-layer4 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_63)
    time.sleep(0.5)

    #9.运行人员补充的工作地点保留带电部分和安全措施
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable4"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_63 = 'document.querySelector("#layui-layer5 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_63)
    time.sleep(0.5)
    
    #保存到草稿箱
    js_aaa = 'document.querySelector("#save").click()'
    driver.execute_script(js_aaa)
    time.sleep(2)
    #关闭
    js_aab = 'document.querySelector("#cancel").click()'
    driver.execute_script(js_aab)
    #time.sleep(3) # 暂停300秒
    #driver.close()
    


    
