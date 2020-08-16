#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/8/16 8:50 上午

import os
import pytest
import allure
import shutil

# allure内层配置 ==》 测试用例内部信息配置

@pytest.fixture(autouse=True)
def set_up():
    print('前置条件：***')
    yield
    print('后置条件：***')

@allure.step('步骤一：打开被测试app')
def one_step():
    pass
@allure.step('步骤二：输入正确的用户名和密码')
def two_step():
    pass

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
    @allure.testcase('http://47.107.178.45/zentao/www/index.php?m=testcase&f=view&caseID=7&version=1','禅道用例地址')
    @allure.issue('http://47.107.178.45/zentao/www/index.php?m=bug&f=view&bugID=405','禅道bug地址')
    @allure.link('http://www.hnxmxit.com',name='湖南软测官网')
    @allure.description('正向场景用例 作者：小明 时间：20200722')
    # @allure.severity('blocker')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sub_01(self):
        one_step()
        two_step()
        # allure.step('f') 不行
        with allure.step('步骤三：点击登录按钮'):
            print('~~ exec test_sub_01 ~~')
        with allure.step('步骤四：点击登录按钮'):
            print('~~ exec test_sub_01 ~~')
        with open(os.path.dirname(__file__)+'/screen_shot/test01.png','rb') as file:
            img_file = file.read()
            allure.attach(img_file,'开班信息',allure.attachment_type.PNG)
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

@allure.epic('[epic]小红电商V1.0')
@allure.feature('[feature]商品模块')
class TestCommodity_01():
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
    pytest.main(['-s','-v','--alluredir=%s'%report_path,'--allure-severities=blocker,critical'])
    os.system('allure generate %s -o %s --clean'%(report_path,report_html_path))

