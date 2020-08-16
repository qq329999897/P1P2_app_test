#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: conftest.py
# @time: 2020/8/16 8:55 上午

import pytest

@pytest.fixture()
def set_up():
    print('测试初始化')
    yield
    print('测试环境清理')