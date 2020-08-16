#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_login_cases.py
# @time: 2020/8/16 9:00 上午

import pytest

class TestLoginCases:
    @pytest.mark.smoketest
    @pytest.mark.logintest
    @pytest.mark.run(order=2)
    def test_login_01(self,module):
        print('~~exec TestLoginCases test_login_01~~')
        assert True

    def test_login_02(self):
        print('~~exec TestLoginCases test_login_02~~')
        assert True

if __name__=='__main__':
    pytest.main(['-s'])