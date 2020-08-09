#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: element_operator_02.py
# @time: 2020/8/9 10:54 上午

import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

current_path = os.path.dirname(__file__)

des = {
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'Samsung Galaxy S9',
    'udid':'192.168.56.101:5555',
    'browserName':'chrome',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)

driver.get('https://www.baidu.com')  # 进入了webview
time.sleep(6)
# print( driver.current_context ) # 获取当前的webview
# print( driver.contexts ) # 获取当前所有的webview
driver.switch_to.context('NATIVE_APP')  # 切换到原生的webview
driver.find_element_by_xpath('//*[@resource-id="com.android.chrome:id/positive_button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"]').click()
time.sleep(2)
driver.switch_to.context('CHROMIUM') # 切换webview
driver.find_element_by_xpath('//input[@id="index-kw"]').send_keys('newdream')
driver.find_element_by_xpath('//button[@id="index-bn"]').click()