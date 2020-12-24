import time
from selenium.webdriver.support.ui import Select

import SinKi
import Fuyong
"""
* 文件名：  RJ_Hyou.py
* 描述：    热力机械工作票新建内容填写
* 创建人：  郭威
* 创建时间：2020-12-19
* 修改人：
* 修改时间：
* 修改内容：。。。。。。
"""

#热力机械工作票
def RJ_Piao(driver):
    driver.implicitly_wait(5)
    #工作班成员
    SinKi.SaGyou_ChengYuan(driver)
    time.sleep(0.3)
    #工作任务:
    driver.find_element_by_xpath(
        "//*[@id='worktask']").send_keys(
            "伊宁市智慧能源有限公司热力机械工作票工作内容!")
    time.sleep(0.1)
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
    #序号1
    SinKi.SaGyou_NaiYou(driver)
    time.sleep(0.5)

    #计划开始时间--计划结束时间
    Fuyong.Plan_start_end(driver)
    time.sleep(0.5)
    
    #5.必须采取的安全措施:
    #5.1. 必须采取的安全措施
    #(1)应停止运行的设备或系统
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable1"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    time.sleep(0.5)
    js_ZTB_51_1 = 'document.querySelector("#layui-layer2 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_51_1)
    time.sleep(0.5)
    
    #（2）应断开下列断路器、隔离开关和熔断器等，并在操作把手（按钮）上设置“禁止合闸 有人工作”安全警示标示牌：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable2"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_51_2 = 'document.querySelector("#layui-layer3 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_51_2)
    time.sleep(0.5)

    JS_Page1 = driver.find_element_by_xpath(
        '//*[@id="all"]/div[2]/table/tbody/tr[14]/td/div/div[1]/div[2]/div[1]/table/thead/tr/th[3]/div[1]')
    #键盘 PAGE_DOWN 按键
    Fuyong.PgDn(driver, JS_Page1)
    time.sleep(0.5)
    
    #（3）应关闭下列截门、挡板（闸板）
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable3"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_51_3 = 'document.querySelector("#layui-layer4 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_51_3)
    time.sleep(0.5)

    #（4）应开启下列阀门、挡板（闸板），使燃烧室、管道、容器内余汽、水、油、烟排放尽，并将温度降至规程规定值：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable4"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_51_4 = 'document.querySelector("#layui-layer5 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_51_4)
    time.sleep(0.5)

    JS_Page1 = driver.find_element_by_xpath(
        '//*[@id="all"]/div[2]/table/tbody/tr[18]/td/div/div[1]/div[2]/div[1]/table/thead/tr/th[3]/div[1]')
    #键盘 PAGE_DOWN 按键
    Fuyong.PgDn(driver, JS_Page1)
    time.sleep(0.5)
    
    #（5）其他安全措施：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable5"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_51_5 = 'document.querySelector("#layui-layer6 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_51_5)
    time.sleep(0.5)

    #5.2 需检修自理的安全措施（加装堵板、作业区域隔离等）：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable6"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_52 = 'document.querySelector("#layui-layer7 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_52)
    time.sleep(0.5)
  
    #5.3 安全注意事项：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable7"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_53 = 'document.querySelector("#layui-layer8 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_53)
    time.sleep(0.5)

    JS_Page1 = driver.find_element_by_xpath(
        '//*[@id="all"]/div[2]/table/tbody/tr[24]/td/div/div[1]/div[2]/div[1]/table/thead/tr/th[3]/div[1]')
    #键盘 PAGE_DOWN 按键
    Fuyong.PgDn(driver, JS_Page1)
    time.sleep(0.5)
    
    #5.5 由热控人员执行的热控措施：
    #定位到要右击的元素
    qqq =driver.find_element_by_xpath('//*[@id="subTable9"]/tbody/tr/td')
    #对定位到的元素执行鼠标右键操作
    Fuyong.MiGi_Click(driver, qqq)
    time.sleep(0.5)
    #粘贴板--输入数据
    Fuyong.ZhanTieban(driver)
    js_ZTB_55 = 'document.querySelector("#layui-layer9 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1").click()'
    driver.execute_script(js_ZTB_55)
    time.sleep(0.5)


    #保存到草稿箱
    Fuyong.Save_Info(driver)
    time.sleep(2)
    #关闭
    Fuyong.Cloose_Info(driver)
    #time.sleep(3) # 暂停300秒
    #driver.close()   

