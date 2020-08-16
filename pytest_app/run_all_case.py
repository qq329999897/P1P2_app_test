#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_case.py
# @time: 2020/8/16 9:19 上午

import pytest

pytest.main(['-s','-m smoketest'])