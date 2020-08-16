#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_login_page_cases.py
# @time: 2020/8/16 9:01 上午

import pytest

class TestLoginPageCases:
    @pytest.mark.smoketest
    @pytest.mark.run(order=1)
    def test_login_page_01(self):
        print('~~ exec TestLoginPageCases test_login_page_01~~')
        assert True

    def test_login_page_02(self):
        print('~~exec TestLoginPageCases test_login_page_02~~')
        assert True