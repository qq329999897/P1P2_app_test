#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/8/16 8:50 上午

import os
import pytest
import allure
import shutil

# allure外层配置

@allure.epic('[epic]小明电商V1.0')
@allure.feature('[feature]登录模块')
class TestLogin():
    @allure.story('[story]不输入用户名和密码')
    @pytest.mark.skip(reason='开发未完善代码，阻碍测试')
    def test_add_01(self):
        print('~~ exec test_add_01 ~~')
        assert True
    @allure.story('[story]正确的登录用户名和密码')
    @allure.title('[case01]使用admin\\123456登录系统')
    def test_sub_01(self):
        print('~~ exec test_sub_01 ~~')
        assert True
    @allure.story('[story]正确的登录用户名和密码')
    @allure.title('[case02]使用tester\\123456登录系统')
    def test_sub_02(self):
        print('~~ exec test_sub_02 ~~')
        assert True

@allure.epic('[epic]小明电商V1.0')
@allure.feature('[feature]商品模块')
class TestCommodity():
    @allure.title('[case01]正常添加商品信息')
    def test_add_01(self):
        print('~~ exec TestDemo05_02 test_add_01 ~~')
        assert True
    def test_add_02(self):
        print('~~ exec TestDemo05_02 test_add_02 ~~')
        assert True


if __name__=='__main__':
    report_path = os.path.dirname(__file__)+'/allure_xml_report'
    report_html_path = os.path.dirname(__file__)+'/allure_html_report'
    if os.path.isdir(report_path):
        shutil.rmtree(report_path)
    os.mkdir(report_path)
    pytest.main(['-s','-v','--alluredir=%s'%report_path])
    os.system('allure generate %s -o %s --clean'%(report_path,report_html_path))