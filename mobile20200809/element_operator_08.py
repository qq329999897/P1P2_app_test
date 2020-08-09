#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: element_operator_02.py
# @time: 2020/8/9 10:54 上午

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

des = {
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'Samsung Galaxy S9',
    'udid':'192.168.56.101:5555',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
time.sleep(2)
e1 = driver.find_element_by_xpath('//android.widget.TextView[@text="设置屏幕锁定"]')
touch_action = TouchAction(driver)
touch_action.press(e1).release().perform()
time.sleep(2)
e2 = driver.find_element_by_xpath('//android.widget.TextView[@text="图案"]')
touch_action.long_press(e2,duration=10000).release().perform()
# 1:295 1335 2: 725 1335  3:725:1755 4: 1145 1335  5: 1145 , 1755
time.sleep(2)
touch_action.long_press(x=295,y=1335).wait(1000)\
            .move_to(x=725,y=1335).wait(1000)\
            .move_to(x=725,y=1755).wait(1000)\
            .move_to(x=1145,y=1335).wait(1000)\
            .move_to(x=1145,y=1755).wait(1000)\
            .release().perform()
