#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: conftest.py
# @time: 2020/8/16 9:05 上午


import pytest
# 包层次（大模块）的conftest 一般是针对各个模块运行一次
@pytest.fixture(scope='module',name='module')
def set_up_module():
    print('~~ test module start run ~~ ')
    yield
    print('~~ test module end run ~~ ')