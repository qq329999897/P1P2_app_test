#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/8/16 8:50 上午

import pytest

pytestmark=pytest.mark.skip()

@pytest.mark.skip(reason='设置测试类不执行')
class TestDemo05_01():
    @pytest.mark.skip(reason='开发未完善代码，阻碍测试')
    def test_add_01(self):
        print('~~ exec test_add_01 ~~')
        assert True
    @pytest.mark.skipif(condition=True,reason='条件满足，用例不执行')
    def test_add_02(self):
        print('~~ exec test_add_02 ~~')
        assert True

    def test_sub_01(self):
        if True:
            pytest.skip('无条件跳过')
        print('~~ exec test_sub_01 ~~')
        assert True
    def test_sub_02(self):
        print('~~ exec test_sub_02 ~~')
        assert True

class TestDemo05_02():
    def test_add_01(self):
        print('~~ exec TestDemo05_02 test_add_01 ~~')
        assert True
    def test_add_02(self):
        print('~~ exec TestDemo05_02 test_add_02 ~~')
        assert True

if __name__=='__main__':
    pytest.main(['-s','-v'])