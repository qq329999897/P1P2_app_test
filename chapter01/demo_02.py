#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_02.py
# @time: 2020/8/5 9:03 下午

from appium import webdriver
import time

des = {
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'Samsung Galaxy S9',
    'udid':'192.168.56.101:5555',
    'browserName':'Browser',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
    # 'chromedirverExcutable':'/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver'
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
driver.implicitly_wait(5)
driver.get('https://www.qq.com')
# time.sleep(20)
driver.find_element_by_xpath('//a[text()="热点"]').click()
# driver.find_element_by_id('index-bn').click()