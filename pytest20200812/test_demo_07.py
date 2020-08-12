#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_01.py
# @time: 2020/8/12 8:56 下午

import pytest

@pytest.fixture(ids=['01','02','03'],params=[100,200,300])
def set_up(request):  # 装饰函数的名称
    return request.param

class TestDemo01:
    def testadd(self,set_up):
        print('exec TestDemo01 testadd')
        assert 100+100 <= set_up

if __name__=='__main__':
    pytest.main(['-v','-s'])  # -s 为了查看 print信息  -v 显示用例详情


