#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: hybrid_locator.py
# @time: 2020/8/9 9:06 上午

from appium import webdriver
import time

des = {
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'Samsung Galaxy S9',
    'udid':'192.168.56.101:5555',
    'appPackage': 'com.ibox.calculators',
    'appActivity': '.CalculatorActivity',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True,
    # 'chromedriverExcutable':'./chromedriver'
    'chromedriverExcutable':'/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver'
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
time.sleep(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.ibox.calculators:id/update_id_cancel"]').click()
time.sleep(2)
driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ibox.calculators:id/toolbox_txt"]').click()
print( driver.contexts )
time.sleep(5)
driver.switch_to.context('WEBVIEW_com.ibox.calculators')
time.sleep(1)
driver.find_element_by_xpath('//p[text()="中华万年历"]').click()