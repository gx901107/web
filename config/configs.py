# -*- coding: utf-8 -*-
# @Time : 2020/12/11 17:25
# @Author : nichao
# @Email : 530504026@qq.com
# @File : configs.py
# @Project : page
import os
BASE_PATH=os.path.dirname(__file__).strip('config')
print(BASE_PATH)
REPORT_PATH=os.path.join(BASE_PATH,'reports')
CASE_PATH=os.path.join(BASE_PATH,'cases')
DATA_PATH=os.path.join(BASE_PATH,'data/logindata.xlsx')