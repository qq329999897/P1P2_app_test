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
    'browserName':'chrome',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True,
    'chromedriverExcutable':'/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver'
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
driver.implicitly_wait(5)
driver.get('http://hao.uc.cn/')
driver.find_element_by_xpath('//input[@class="search-input"]').send_keys('newdream')
driver.find_element_by_xpath('//button[@class="search-btn"]').click()
# 元素识别方法 以selenium之前学习过的为主

