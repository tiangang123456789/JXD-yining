import time
from selenium.webdriver.support.ui import Select
from datetime import datetime

import random   ##导入随机数模块
import Fuyong
"""
* 文件名：  SinKi.py
* 描述：    伊宁电厂 工作票共通
* 创建人：  郭威
* 创建时间：2020-12-21
"""
#新建票定位到右侧面板
def Migi_Div(driver):
    driver.switch_to.frame(
    driver.find_element_by_xpath(
        "//iframe[starts-with(@tab-id, '2')]"))

#选择工作票类型
    """
    hyou_number=1,热控工作票票；
    hyou_number=2,热力机械工作票；
    hyou_number=3,三合一工作票；
    """
def Hyou_type(driver, hyou_number):
    if hyou_number == 1:
        driver.find_element_by_xpath(
            '//dd[@lay-value="热控工作票"]').click()        
    elif hyou_number == 2:
        driver.find_element_by_xpath(
            '//dd[@lay-value="热力机械工作票"]').click()        
    elif hyou_number ==3:
        driver.find_element_by_xpath(
            '//dd[@lay-value="三票合一工作票"]').click()
        
#(开票前需要填写的)工作内容
    """
    hyou_number=1,热控工作票票；
    hyou_number=2,热力机械工作票；
    hyou_number=3,三合一工作票；
    """
def KaiPiao_naiyou(driver, hyou_number):
    ShiJian = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if hyou_number == 1:
        driver.find_element_by_xpath(
            "//*[@id='ticketcontent']").send_keys(
                '热控工作票'+ShiJian)
    elif hyou_number == 2:
        driver.find_element_by_xpath(
            "//*[@id='ticketcontent']").send_keys(
                '热力机械工作票'+ShiJian)
    elif hyou_number == 3:
        driver.find_element_by_xpath(
            "//*[@id='ticketcontent']").send_keys(
                '三票合一工作票'+ShiJian)
    else :
        driver.find_element_by_xpath(
            "//*[@id='ticketcontent']").send_keys(
                '未知工作票'+ShiJian)

#(开票前选择的)机组
    """
<dl class="layui-anim layui-anim-upbit" style="">
<dd lay-value="" class="layui-select-tips layui-this">请选择</dd>
<dd lay-value="7F29ADC6-8A12-3B87-26DB-4FD9034608AE" class="">#1机组</dd>
<dd lay-value="4F8B380F-6AD2-3649-F090-B6F1D6DB7AEB" class="">#2机组</dd>
<dd lay-value="D33B5C8A-CDE0-E4EF-F4DF-84468E4C1111" class="">#1锅炉</dd>
<dd lay-value="D33B5C8A-CDE0-E4EF-F4DF-84468E4C2222" class="">#2锅炉</dd>
<dd lay-value="D33B5C8A-CDE0-E4EF-F4DF-84468E4C3333" class="">#3锅炉</dd></dl>
    """
def JiZu_name(driver, jizu_number):
    ShiJian = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if jizu_number == 1:
        driver.find_element_by_xpath(
            '//*[@lay-value="7F29ADC6-8A12-3B87-26DB-4FD9034608AE"]').click()
    elif jizu_number == 2:
        driver.find_element_by_xpath(
            '//*[@lay-value="4F8B380F-6AD2-3649-F090-B6F1D6DB7AEB"]').click()
    elif jizu_number == 3:
        driver.find_element_by_xpath(
            '//*[@lay-value="D33B5C8A-CDE0-E4EF-F4DF-84468E4C1111"]').click()
    elif jizu_number == 4:
        driver.find_element_by_xpath(
            '//*[@lay-value="D33B5C8A-CDE0-E4EF-F4DF-84468E4C2222"]').click()
    else :
        driver.find_element_by_xpath(
            '//*[@lay-value="D33B5C8A-CDE0-E4EF-F4DF-84468E4C3333"]').click()


#(开票前选择的)专业
    """
<dl class="layui-anim layui-anim-upbit" style="">
<dd lay-value="" class="layui-select-tips layui-this">请选择</dd>
<dd lay-value="DD6C2AFA-E40C-1B0D-524B-CAEFCFDE3DF7" class="">电气</dd>
<dd lay-value="68D94B7E-F837-C6D4-FB09-09DDAB3C38EA" class="">汽机</dd>
<dd lay-value="B398E3C2-15EF-D38B-324B-AECFE6E19BD5" class="">锅炉</dd>
<dd lay-value="EC98A204-2265-D295-9B80-02E183461B1D" class="">热控</dd>
<dd lay-value="44EB030F-0AEF-CF3D-B02A-A679F29133E4" class="">化水</dd>
<dd lay-value="56965294-4FD7-3E40-8840-44E1631FD3F0" class="">脱硫脱硝</dd>
<dd lay-value="3E96EF2E-28D2-43EB-6371-FF8FF57B0055" class="">输煤</dd>
<dd lay-value="4A6S88D7A414687ASD6874D6AW468AEWE" class="">除灰</dd>
<dd lay-value="1A64D68WE1654D6AD365S4D6A8SDA64QT" class="">土建</dd></dl>
    """
def ZhuanYe_name(driver, zhuanye_number):
    if zhuanye_number == 1:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[2]').click()
    elif zhuanye_number == 2:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[3]').click()
    elif zhuanye_number == 3:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[4]').click()
    elif zhuanye_number == 4:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[5]').click()
    elif zhuanye_number == 5:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[6]').click()
    elif zhuanye_number == 6:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[7]').click()
    elif zhuanye_number == 7:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[8]').click()
    elif zhuanye_number == 8:
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[9]').click()
    else :
        driver.find_element_by_xpath(
            '//*[@id="div_workapprivaldeptname"]/div[2]/div/div/dl/dd[10]').click()

#工作班成员
def SaGyou_ChengYuan(driver):
    #工作班成员
    DoubleSB = driver.find_element_by_xpath(
        "//*[@id='totalstaff']")
    #双击
    Fuyong.Double2_Click(driver,DoubleSB)
    time.sleep(0.5)
    #人员树全选
    driver.find_element_by_xpath(
        "//*[@id='1_anchor']/i[1]").click()
    
    time.sleep(0.3)
    #点击保存
    #利用js来获取元素位置
    js = 'document.querySelector("#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js)
'''
    #这是随机数测试↓
    while True :
        Workers(driver)
        time.sleep(0.3)
        #点击保存
        #利用js来获取元素位置
        js = 'document.querySelector("#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
        driver.execute_script(js)
        aaa = driver.find_element_by_xpath('//*[@id="totalstaff"]')
        print(aaa.get_attribute('value')) # 获取输入框中的文本
        if not aaa.strip() :
            break
    #这是随机数测试↑
'''
    
'''
#人员树随机选择
def Workers(driver):
        suiji = random.randint(3, 7)
        if suiji < 10:
            driver.find_element_by_xpath(f'//*[starts-with(@id="yn000{suiji}")]').click()
        elif 10 <= suiji < 100:
            driver.find_element_by_xpath(f'//*[@id="yn00{suiji}"]').click()
        elif 100 <= suiji < 1000:
            driver.find_element_by_xpath(f'//*[@id="yn0{suiji}"]').click()
        else :
            driver.find_element_by_xpath(f'//*[@id="yn{suiji}"]').click()
 '''
#添加工作内容
def SaGyou_NaiYou(driver):
    #序号1
    #利用js点击'工作地点及设备名称'文本框
    js_DD1 = 'document.querySelector("#subTable11 > tbody > tr:nth-child(1) > td:nth-child(3)").click()'
    driver.execute_script(js_DD1)
    #找到'工作地点及设备名称'的元素id，输入
    DD1 = driver.find_element_by_xpath(
        '//*[@id="subTable11"]/tbody/tr[1]/td[3]')
    DD1.send_keys("工作地点及设备名称1")
    #模拟键盘Tab按键
    Fuyong.Tab_Key(driver,DD1)
    time.sleep(0.5)
    #利用js选中序号1复选框
    js_XH1 = 'document.querySelector("#subTable11 > tbody > tr:nth-child(1) > td.bs-checkbox > input[type=checkbox]").click()'
    driver.execute_script(js_XH1)
    time.sleep(0.5)
    #利用js点击'负责人'文本框
    js_FZR1 = 'document.querySelector("#subTable11 > tbody > tr:nth-child(1) > td:nth-child(5)").click()'
    driver.execute_script(js_FZR1)
    #找到'负责人'的元素id，输入
    FZR1 = driver.find_element_by_xpath(
        '//*[@id="subTable11"]/tbody/tr[1]/td[5]')
    FZR1.send_keys("负责人1")
    time.sleep(0.5)
    #模拟键盘Tab按键
    Fuyong.Tab_Key(driver,FZR1)

#添加多条工作内容
#time.sleep(1.5)
def Add_Naiyou(driver):
    for Add_naiyou in (1,3):
        driver.find_element_by_xpath(
        "//*[@id='addRow11']").click()
    time.sleep(1.5)

#添加三合一工作内容
def SaGyou_NaiYou1(driver):
    #序号1
    #利用js点击'工作地点及设备名称'文本框
    js_DD1 = 'document.querySelector("#subTable11 > tbody > tr:nth-child(1) > td:nth-child(3)").click()'
    driver.execute_script(js_DD1)
    #找到'工作地点及设备名称'的元素id，输入
    DD1 = driver.find_element_by_xpath(
        '//*[@id="subTable11"]/tbody/tr[1]/td[3]')
    DD1.send_keys("工作地点及设备名称1")
    #模拟键盘Tab按键
    Fuyong.Tab_Key(driver,DD1)
    time.sleep(0.5)
    #利用js选中序号1复选框
    js_XH1 = 'document.querySelector("#subTable11 > tbody > tr:nth-child(1) > td.bs-checkbox > input[type=checkbox]").click()'
    driver.execute_script(js_XH1)
    time.sleep(0.5)
    #利用js点击'负责人'文本框
    js_FZR1 = 'document.querySelector("#subTable11 > tbody > tr:nth-child(1) > td:nth-child(5)").click()'
    driver.execute_script(js_FZR1)
    #找到'负责人'的元素id，输入
    FZR1 = driver.find_element_by_xpath(
        '//*[@id="subTable11"]/tbody/tr[1]/td[5]')
    FZR1.send_keys("负责人1")
    time.sleep(0.5)
    #模拟键盘Tab按键
    Fuyong.Tab_Key(driver,FZR1)












































