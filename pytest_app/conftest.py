#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: conftest.py
# @time: 2020/8/16 9:05 上午


import pytest
# 顶层（项目）的conftest 一般是针对各个子包运行一次的
@pytest.fixture(scope='package',autouse=True)
def set_up_package():
    print('~~ test package start run ~~ ')
    yield
    print('~~ test package end run ~~ ')