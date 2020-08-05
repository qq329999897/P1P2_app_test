#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/7/26 5:02 下午

from  appium import webdriver
import time


des = {
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'Samsung Galaxy S9',
    'udid':'192.168.56.101:5555',
    'appPackage':'com.android.calculator2',
    'appActivity':'.Calculator',
    'noReset': True,
    'unicodeKeyboard': True,  # 输入支持中文
    'resetKeyboard': True
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
driver.find_element_by_id( 'com.android.calculator2:id/digit_9' ).click()
time.sleep(1)
# driver.find_element_by_class_name( 'android.widget.Button' ).click()
# driver.find_element_by_accessibility_id('删除').click()
# driver.find_element_by_id('DEL').click()
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.Button[5]').click()
# 属性定位 //类名[@属性名='属性值']
# driver.find_element_by_xpath('//android.widget.Button[ @text="9" ]').click()
# 多属性定位  //类名[@属性名='属性值' and/or @属性名='属性值' ....]
# driver.find_element_by_xpath('//android.widget.Button[ @text="9" and @index="2"]').click()
# 部分属性值定位  com.android.calculator2:id/digit_9
# driver.find_element_by_xpath('//android.widget.Button[ contains(@resource-id,"digit_9") ]').click()
# driver.find_element_by_xpath('//android.widget.Button[ ends-with(@resource-id,"digit_9") ]').click()

# UIAutomator
# driver.find_element_by_android_uiautomator( 'text("9")' ).click()
# driver.find_element_by_android_uiautomator( 'new UiSelector().textContains("9")' ).click()
# driver.find_element_by_android_uiautomator('resourceId("com.android.calculator2:id/digit_9")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/digit_9")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().description("删除")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("8")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/pad_numeric").childSelector(className("android.widget.Button").instance(5))').click()
# driver.find_element_by_android_uiautomator( 'new UiSelector().resourceId("com.android.calculator2:id/digit_9").fromParent(text("8"))' ).click()