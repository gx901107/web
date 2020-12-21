# -*- coding: utf-8 -*-
# @Time : 2020/12/11 16:37
# @Author : nichao
# @Email : 530504026@qq.com
# @File : browser.py
# @Project : page
from selenium import webdriver
def browser_chrome():
    driver=webdriver.Chrome()
    driver.maximize_window()
    return driver