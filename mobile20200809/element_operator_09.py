#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: element_operator_02.py
# @time: 2020/8/9 10:54 上午

import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

current_path = os.path.dirname(__file__)

des = {
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'Samsung Galaxy S9',
    'udid':'192.168.56.101:5555',
    # 'appPackage': 'com.android.settings',
    # 'appActivity': '.Settings',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
if driver.is_app_installed('com.ibox.calculators'):
    driver.remove_app('com.ibox.calculators')
driver.install_app( os.path.join(current_path,'jisuanqi_587.apk') )
driver.start_activity('com.ibox.calculators','.CalculatorActivity')
time.sleep(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.ibox.calculators:id/update_id_cancel"]').click()
time.sleep(2)
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.ibox.calculators:id/digit9"]').click()
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.ibox.calculators:id/plus"]').click()
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.ibox.calculators:id/digit7"]').click()
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.ibox.calculators:id/equal"]').click()
driver.close_app()
time.sleep(2)
driver.remove_app('com.ibox.calculators')