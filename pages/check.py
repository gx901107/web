# -*- coding: utf-8 -*-
# @Time : 2020/12/15 21:41
# @Author : nichao
# @Email : 530504026@qq.com
# @File : check.py
# @Project : page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from model.browser import browser_chrome
class Check(BasePage):
    check_locator = (By.CSS_SELECTOR,
"#listDiv > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(11) > a:nth-child(1) > img")  # 查看按钮

    def check_element(self):
        """
        获取【查看】按钮元素
        :return:
        """
        return self.findelement(self.check_locator)
    def checkshop(self):
        self.check_element().click()