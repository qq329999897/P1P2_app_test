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
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
# driver.tap([(614,1566)],1000)
# driver.tap([(614,1566),(723,1064),(548,2081),(832,1334)],1000)
# e1 = driver.find_element_by_xpath('//android.widget.TextView[@text="存储"]')
# e2 = driver.find_element_by_xpath('//android.widget.TextView[@text="应用和通知"]')
# driver.scroll(e1,e2,3000)
# driver.flick(614,1566,548,1566)  # press   driver.flick(614,1566,66,0)
size = driver.get_window_size()
# driver.swipe(1440/2,2960/2,1440/2,2960/4,3000)
driver.swipe(size['width']/2,size['height']/2,size['width']/2,size['height']/4,3000)

# 函数  屏幕分辨率知道 x   y      447  1426  == ?   447/x*100 ==    1426 / y *100

# def calc( x,y ):
#     return (x/1440.0,y/2960.0)
# print( calc(447,1426) )
#
# 1980*0.31= ? 2560*0.48= ?
