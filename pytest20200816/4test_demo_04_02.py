#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/8/16 8:50 上午

import pytest

@pytest.mark.run(order=4)
def test_add_01():
    print('~~ exec test_add_01 ~~')
    assert True
@pytest.mark.run(order=1)
def test_add_02():
    print('~~ exec test_add_02 ~~')
    assert True
@pytest.mark.run(order=3)
def test_sub_01():
    print('~~ exec test_sub_01 ~~')
    assert True
@pytest.mark.run(order=2)
def test_sub_02():
    print('~~ exec test_sub_02 ~~')
    assert True

if __name__=='__main__':
    pytest.main(['-s','-v'])