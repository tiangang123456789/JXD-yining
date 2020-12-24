import Fuyong

"""
* 文件名：  Login.py
* 描述：    系统主页；用户名密码
* 创建人：  郭威
* 创建时间：2020-12-21
"""


#系统链接
def YiNing_login(driver):
    #隐示等待
    driver.implicitly_wait(5)
    # 最大化浏览器窗口
    driver.maximize_window()
    # 打开”运营管理“页面
    #driver.get("http://192.168.2.114:8180/login")
    driver.get("http://192.168.2.169:8097")
    # 打印标题
    print(driver.title)

#用户名--密码
    """
    hyou_number=1,热控工作票票；
    hyou_number=2,热力机械工作票；
    hyou_number=3,三合一工作票；
    """
def Users_Pwd(driver, hyou_number):
    #隐示等待
    driver.implicitly_wait(5)
    if hyou_number == 1:        
        # 输入用户名
        Fuyong.UserName(driver, "qxjun")
        # 输入密码
        Fuyong.Pwd(driver, "123456")
        # 进入运营管理系统
        Fuyong.Sys_tem(driver)
    elif hyou_number ==2:
        # 输入用户名
        Fuyong.UserName(driver, "zjxin")
        # 输入密码
        Fuyong.Pwd(driver, "123456")
        # 进入运营管理系统
        Fuyong.Sys_tem(driver)
    elif hyou_number ==3:
        # 输入用户名
        Fuyong.UserName(driver, "srui")
        # 输入密码
        Fuyong.Pwd(driver, "123456")
        # 进入运营管理系统
        Fuyong.Sys_tem(driver)
    else: #设置一个通用用户
        # 输入用户名
        Fuyong.UserName(driver, "yling")
        # 输入密码
        Fuyong.Pwd(driver, "123456")
        # 进入运营管理系统
        Fuyong.Sys_tem(driver)
