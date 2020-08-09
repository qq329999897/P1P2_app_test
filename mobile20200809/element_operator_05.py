#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: element_operator_02.py
# @time: 2020/8/9 10:54 上午

import time
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

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
print( driver.network_connection ) # 查看网络
time.sleep(2)
# driver.set_network_connection(1)
driver.set_network_connection( ConnectionType.ALL_NETWORK_ON ) # 设置网络方式

driver.save_screenshot('./test1.png') # 截图
print( driver.get_device_time() )  #获取时间
