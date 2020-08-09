#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: element_operator_02.py
# @time: 2020/8/9 10:54 上午

from appium import webdriver
import time

des = {
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'Samsung Galaxy S9',
    'udid':'192.168.56.101:5555',
    'appPackage': 'com.android.dialer',
    'appActivity': '.app.DialtactsActivity',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)


value = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.android.dialer:id/emptyListViewAction"]').get_attribute("displayed")
print(value,type(value),)
value = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.android.dialer:id/emptyListViewAction"]').is_displayed()
print(value)
