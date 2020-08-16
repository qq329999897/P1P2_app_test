#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/8/16 8:50 上午

import pytest

def test_sub():
    print('~~ exec test_sub ~~')
    assert True

if __name__=='__main__':
    pytest.main(['-s'])