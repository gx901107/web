# -*- coding: utf-8 -*-
# @Time : 2020/12/11 16:58
# @Author : nichao
# @Email : 530504026@qq.com
# @File : runlogin.py
# @Project : page
from BeautifulReport import BeautifulReport
from config.configs import CASE_PATH,REPORT_PATH
import time
import unittest
discover=unittest.defaultTestLoader.discover(CASE_PATH,'case.py')
BeautifulReport(discover).report(description="自动化测试报告",report_dir=REPORT_PATH,
                          filename=time.strftime("%Y-%m-%d %H_%M_%S"))
