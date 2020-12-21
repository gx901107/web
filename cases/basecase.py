# -*- coding: utf-8 -*-
# @Time : 2020/12/11 20:34
# @Author : nichao
# @Email : 530504026@qq.com
# @File : basecase.py
# @Project : page
import unittest
from model.browser import browser_chrome
class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=browser_chrome()

    def tearDown(self) -> None:
        self.driver.quit()