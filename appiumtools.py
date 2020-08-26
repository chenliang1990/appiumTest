from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

def find_element(driver, locator, timeout=30):
    """
        方法名：动态查找元素:显式等待
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - ("id", "username")    # find_xx_by_id
                    - ("aid", "username")   # find_xxx_by_accessbility_id
                    - ("text", "username")  # find_element_by_android_uiautomator
                    - ("xpath", "username") # xpath
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：返回元素
            - 没找到元素：直接报错:timeout
    """
    if locator[0] == "aid":
        locator = (MobileBy.ACCESSIBILITY_ID, locator[1])
    
    if locator[0] == "text":
        print(locator)
        locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(locator[1]))
        print(locator)

    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))


def is_element_cunzai(driver, locator):
    try:
        find_element(driver, locator)
        return True
    except:
        return False