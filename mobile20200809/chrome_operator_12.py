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
    'appPackage': 'com.wondertek.paper',
    'appActivity': 'cn.thepaper.paper.ui.main.MainActivity',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
time.sleep(10)
print( driver.contexts )
driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"黎智英被捕案")]').click()
time.sleep(8)
driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.wondertek.paper:id/post_comment"]').click()
time.sleep(3)
driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.wondertek.paper:id/edit"]').send_keys('hello')
time.sleep(3)
driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.wondertek.paper:id/confirm"]').click()
