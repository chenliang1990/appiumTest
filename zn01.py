from appium import webdriver  # 导入appium第三方包
from appiumtools import find_element
import time
# 1. 打开app，获取手机的把柄
desired_caps = {}
desired_caps['platformName'] = 'Android'              # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '7.1.2'             # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'MI 4LTE'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'uni.UNI06649C8'         # app的名字：也叫包名，软件的包名是唯一的
                                                      # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                      # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = 'io.dcloud.PandoraEntryActivity'# 同上↑,activity：软件启动页面的id
desired_caps['unicodeKeyboard'] = True                # 为了支持中文
desired_caps['resetKeyboard'] = True                  # 设置成appium自带的键盘
desired_caps['noReset'] = True                        # 使用缓存，避免重新登录
# 去打开app，并且返回当前app的操作对象
# http://localhost:4723/wd/hub : appium desktop提供的
# desired_caps: 手机app信息的字典
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
# 没有办法定位元素，就点坐标
driver.tap([(354,1088)])
time.sleep(5)
# 文本值定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
my_btn = ("text","我的")
find_element(driver,my_btn).click()
# 不过正常做app测试是不需要做登录的，直接账号输入进去之后，设置好desired_caps['noReset'] = True
# 这个，就可以使用缓存，避免重新登录了，所以登录这个功能是不需要去做自动化的