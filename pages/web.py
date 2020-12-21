# -*- coding: utf-8 -*-
# @Time : 2020/12/15 17:21
# @Author : nichao
# @Email : 530504026@qq.com
# @File : web.py
# @Project : page
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Assert(BasePage):
    _url = BasePage._url + "/upload/user.php"
    loginbotton_locator = (By.XPATH, '//*[@id="ECS_MEMBERZONE"]/a[1]')  # 首页登录按钮
    username_locator = (By.NAME, 'username')  # 定位用户名输入框
    password_locator = (By.NAME, 'password')  # 定位密码输入框
    submit_locator = (By.NAME, 'submit')  # 提交登录点击按钮
    websearch_locator = (By.XPATH, '//*[@id="keyword"]')  # 搜索按钮输入框
    websearchbutton_locator = (By.CSS_SELECTOR, "#searchForm > span.ipt2 > input")  # 【搜索】按钮
    assertvalue_locator = (By.XPATH, '//*[@id="compareForm"]/div/div/p/a')

    def loginbotton_element(self):
        """
        首页登录按钮元素
        :return:
        """
        return self.findelement(self.loginbotton_locator)

    def username_element(self):
        """
        用户名输入框元素
        :return:
        """
        return self.findelement(self.username_locator)

    def password_element(self):
        """
        密码输入框元素
        :return:
        """
        return self.findelement(self.password_locator)

    def submit_element(self):
        """
        提交登录元素
        :return:
        """
        return self.findelement(self.submit_locator)

    def websearch_element(self):
        return self.findelement(self.websearch_locator)

    def websearchbutton_element(self):
        return self.findelement(self.websearchbutton_locator)

    def assertvalue_element(self):
        return self.findelement(self.assertvalue_locator)

    def assertion(self):
        self.open()
        self.loginbotton_element().click()
        self.username_element().send_keys("张可爱3")
        self.password_element().send_keys("admin123")
        self.submit_element().click()
        sleep(4)
        self.websearch_element().send_keys("森林公园")
        sleep(2)
        self.websearchbutton_element().click()
        sleep(2)
        return self.assertvalue_element().text
