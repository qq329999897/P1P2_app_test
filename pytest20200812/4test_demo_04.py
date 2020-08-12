#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_01.py
# @time: 2020/8/12 8:56 下午

import pytest

@pytest.fixture(scope='module')
def set_up():
    print('测试初始化')
    yield
    print('测试环境清理')

class TestDemo01:
    def testadd(self,set_up):
        print('exec test_demo_04 TestDemo01 testadd')
        assert 10+10 == 20
    def testsub(self,set_up):
        print('exec test_demo_04 TestDemo01 testsub')
        assert 10-10 == 20

class TestDemo02:
    def testadd(self,set_up):
        print('exec test_demo_04 TestDemo02 testadd')
        assert 10+10 == 20
    def testsub(self,set_up):
        print('exec test_demo_04 TestDemo02 testsub')
        assert 10-10 == 20

if __name__=='__main__':
    pytest.main(['-s'])  # -s 为了查看 print信息


