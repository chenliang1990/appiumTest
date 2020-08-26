from appium import webdriver  # 导入appium第三方包
# 1. 打开app，获取手机的把柄
desired_caps = {}
desired_caps['platformName'] = 'Android'              # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '7.1.2'             # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'MI 4LTE'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis' # app的名字：也叫包名，软件的包名是唯一的
                                                      # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                      # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.ApiDemos'             # 同上↑,activity：软件启动页面的id
desired_caps['unicodeKeyboard'] = True                # 为了支持中文
desired_caps['resetKeyboard'] = True                  # 设置成appium自带的键盘
desired_caps['noReset'] = True                        # 使用缓存，避免重新登录
# 去打开app，并且返回当前app的操作对象
# http://localhost:4723/wd/hub : appium desktop提供的
# desired_caps: 手机app信息的字典
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 2. 定位元素
# accessibility_id定位
# driver.find_element_by_accessibility_id("App").click()
# 文本值定位
driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()
driver.find_element_by_accessibility_id("Search").click()
driver.find_element_by_accessibility_id("Invoke Search").click()
# id定位：安卓中不唯一
driver.find_element_by_id('io.appium.android.apis:id/txt_query_prefill').send_keys("学习测试很好")
# 第一种断言：使用find_elements来判断
# e = driver.find_elements_by_id('io.appium.android.apis:id/txt_query_appdata')
# if len(e) != 0:
#     print("执行测试用例成功")
# else:
#     print("执行测试用例失败!")

# 第二种，使用try来判断
try:
    driver.find_element_by_id('io.appium.android.apis:id/txt_query_appdata')
    print("执行测试用例成功")
except:
    print("执行测试用例失败!")
driver.quit()
# xpath定位
# driver.find_element_by_xpath('//android.widget.TextView[@content-desc="App"]').click()

