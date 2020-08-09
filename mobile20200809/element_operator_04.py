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

print(  driver.is_locked() ) # 判断是否锁屏
driver.lock(3)   # 3秒之后锁屏
time.sleep(5)
print(  driver.is_locked() )
time.sleep(2)
driver.unlock()
time.sleep(2)
driver.open_notifications()  # 打开通知栏
time.sleep(3)
driver.orientation = 'LANDSCAPE' #横竖屏切换
time.sleep(3)
driver.orientation = 'PORTRAIT'

value = driver.get_window_size() # 获取手机屏幕分辨率
print( value )
