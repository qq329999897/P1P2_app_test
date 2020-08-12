#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_01.py
# @time: 2020/8/12 8:56 下午

import pytest

class TestDemo01:
    def testadd(self):
        assert 10+10 == 20

if __name__=='__main__':
    pytest.main()
