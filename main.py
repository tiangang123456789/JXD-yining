from selenium import webdriver

import Login
import Hyou


"""
* 文件名：  main.py
* 描述：    伊宁电厂ver1.0
* 创建人：  郭威
* 创建时间：2020-12-19
"""

if __name__ == '__main__':
    print('这是主函数：')
    print("选择需要新建的工作票：")
    print("  1.工作票--新建工作票--热控工作票")
    print("  2.工作票--新建工作票--热力机械工作票")
    print("  3.工作票--新建工作票--三票合一工作票")
    print("  4.退出")
    hyou_number = int(input("输入数字选择工作票: "))
    print("选择机组：\n  1.#1机组  2.#2机组  3.#1锅炉  4.#2锅炉  5.#3锅炉")
    jizu_number = int(input("输入数字选择机组: "))
    print("选择专业：\n  1.电气  2.汽机  3.锅炉  4.热控  5.化水  6.脱硫脱硝  7.输煤  8.除灰  9.土建")
    zhuanye_number = int(input("输入数字选择专业: "))
    if hyou_number == 4:
        quit()
    else :
        # 创建一个Chrome浏览器的webdriver实例
        driver = webdriver.Chrome()
        #隐示等待
        driver.implicitly_wait(5)
        Login.YiNing_login(driver)
        Hyou.Hard_List(driver, hyou_number, jizu_number, zhuanye_number)
