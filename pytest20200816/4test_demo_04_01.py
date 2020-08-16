#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/8/16 8:50 上午

import pytest

def test_add_01():
    print('~~ exec test_demo_04_01 test_add_01 ~~')
    assert True
def test_add_02():
    print('~~ exec test_demo_04_01 test_add_02 ~~')
    assert True
@pytest.mark.run(order=5)
def test_sub_01():
    print('~~ exec test_demo_04_01 test_sub_01 ~~')
    assert True
@pytest.mark.last
def test_sub_02():
    print('~~ exec test_demo_04_01 test_sub_02 ~~')
    assert True



if __name__=='__main__':
    pytest.main(['-s'])