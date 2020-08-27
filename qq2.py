import time,requests, json, traceback, os
from appium import webdriver as aw 
from appiumtools import find_element
from selenium import webdriver as sw
from seleniumtools import find_element
from appiumtools import find_element as afind
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def get_chat_msg_by_xiaobing(driver1, word):
    if driver1 == None:
        driver1 = sw.Chrome(executable_path='chromedriver.exe')
        driver1.get("https://api.weibo.com/chat/#/chat?source_from=5")

        driver1.delete_all_cookies()
		cookies = []
        for a in cookies:
            driver1.add_cookie(a)
        driver1.refresh()

        xiaobing = ('xpath', '//*[@id="app"]/div/div/div[1]/div[3]/div/div[1]/div/div/ul/li')
        find_element(driver1, xiaobing).click()

        time.sleep(1)
        msg_box = ('id', 'webchat-textarea')
        e = find_element(driver1, msg_box)
        e.send_keys(word)
        e.send_keys(Keys.ENTER)
        # time.sleep(2)
        # chat_content = ('class name', 'chat-content')
        # e = find_element(driver1, chat_content)
        time.sleep(2)
        chat_content = ('class name', 'chat-content')
        e = find_element(driver1, chat_content)
        if e.text.split('\n')[-1] == word:
            time.sleep(1)
            chat_content = ('class name', 'chat-content')
            e = find_element(driver1, chat_content)
        return driver1,e.text.split('\n')[-1]

        return driver1,e.text.split('\n')[-1]
    else:
        xiaobing = ('xpath', '//*[@id="app"]/div/div/div[1]/div[3]/div/div[1]/div/div/ul/li')
        find_element(driver1, xiaobing).click()

        time.sleep(1)
        msg_box = ('id', 'webchat-textarea')
        e = find_element(driver1, msg_box)
        e.send_keys(word)
        e.send_keys(Keys.ENTER)
        time.sleep(2)
        chat_content = ('class name', 'chat-content')
        e = find_element(driver1, chat_content)
        if e.text.split('\n')[-1] == word:
            time.sleep(1)
            chat_content = ('class name', 'chat-content')
            e = find_element(driver1, chat_content)
        return driver1,e.text.split('\n')[-1]


def get_chat_msg(word):

    KEY = '29ca2626d4d84304a7fc16241057878d'    # change to your API KEY
    url = 'http://www.tuling123.com/openapi/api' 

    req_info = word.encode('utf-8')

    query = {'key': KEY, 'info': req_info}
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

    r = requests.post(url, params=query, headers=headers)
    res = r.text
    return (json.loads(res).get('text').replace('<br>', '\n'))


driver1 = None
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

driver = aw.Remote('http://localhost:4725/wd/hub', desired_caps)


chat_list_root = ('id', 'com.tencent.mobileqq:id/recent_chat_list')
root = afind(driver, chat_list_root)
root.find_elements_by_id('com.tencent.mobileqq:id/relativeItem')[0].click()

while True:
    send_msg = "appium机器人正在升级中..." 
    last_text_msg = 'com.tencent.mobileqq:id/chat_item_content_layout'
    last_imag_msg = 'com.tencent.mobileqq:id/pic'
    root_list = ('id','com.tencent.mobileqq:id/listView1')
    root = afind(driver, root_list)
     
    try:
        # 判断最后一条消息是否是自己的，如果是，就跳过
        father = root.find_elements_by_id('com.tencent.mobileqq:id/a6b')[-1] # 找到所有的根据
        avj = ('id', 'com.tencent.mobileqq:id/avj')
        nickname = ('id', 'com.tencent.mobileqq:id/chat_item_nick_name')
        avj = afind(father, avj)
        nickname = afind(avj, nickname)

        if nickname.text == "大侠王尼玛":
            print("这是自己的话，跳过")
            continue

        text_msg, imgs_msg = None, None
        last_imag_msg = 'com.tencent.mobileqq:id/pic'
        last_text_msg = 'com.tencent.mobileqq:id/chat_item_content_layout'
        try:
            imgs_msg = father.find_element_by_id(last_imag_msg)
            send_msg = "兄弟们，这是表情包啊"
        except:
            text_msg = father.find_element_by_id(last_text_msg)

        if text_msg is not None:
            try:
                # send_msg = get_chat_msg(text_msg[-1].text) #图灵机器人
                driver1, send_msg = get_chat_msg_by_xiaobing(driver1, text_msg.text)
            except Exception as e:
                print("报错了，跳过")
                traceback.print_exc()
                continue

        driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(send_msg)
        driver.find_element_by_id('com.tencent.mobileqq:id/fun_btn').click()
    except Exception as e :
        print("机器人竟然崩溃...")
        traceback.print_exc()
