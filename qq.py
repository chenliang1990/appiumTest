import time,requests, json
from appium import webdriver  
from appiumtools import find_element, is_element_cunzai

def get_chat_msg(word):

    KEY = '29ca2626d4d84304a7fc16241057878d'    # change to your API KEY
    url = 'http://www.tuling123.com/openapi/api' 

    req_info = word.encode('utf-8')

    query = {'key': KEY, 'info': req_info}
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

    r = requests.post(url, params=query, headers=headers)
    res = r.text
    return (json.loads(res).get('text').replace('<br>', '\n'))

if __name__ == "__main__":
    desired_caps = {}
    desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = '5.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = 'MI 4LTE'                      # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = 'com.tencent.mobileqq'               # app的名字：
                                                            # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                            # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
    desired_caps['appActivity'] = '.activity.SplashActivity'              # 同上↑
    desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
    desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
    desired_caps['noReset'] = True                        # 使用app缓存

    # 去打开app，并且返回当前app的操作对象
    # http://localhost:4723/wd/hub ：appium desktop提供的
    # desired_caps：手机、app信息的字典
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    time.sleep(10)
    driver.tap([(521,507)])
    time.sleep(1)

    while True:
        send_msg = "appium机器人正在升级中..."
        last_text_msg = 'com.tencent.mobileqq:id/chat_item_content_layout'
        last_imag_msg = 'com.tencent.mobileqq:id/pic'

        try:
            text_msg = driver.find_elements_by_id(last_text_msg)

            # 判断最后一条消息是否是自己的，如果是，就跳过
            if text_msg[-1].location['x'] != 162:
                print("这是自己的话，跳过")
                time.sleep(3)
                continue
                

            if len(text_msg) == 0:
                send_msg = "兄弟们，最后一条消息是表情包啊"
            else:
                try:
                    send_msg = get_chat_msg(text_msg[-1].text)
                except:
                    print("报错了，跳过把")
                    continue
        
            driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(send_msg)
            driver.find_element_by_id('com.tencent.mobileqq:id/fun_btn').click()
        except:
            print("机器人竟然崩溃...")
        time.sleep(5)
