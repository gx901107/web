# -*- coding: utf-8 -*-
# @Time : 2020/12/15 20:56
# @Author : nichao
# @Email : 530504026@qq.com
# @File : searchshop.py
# @Project : page
from time import sleep

from selenium import webdriver
from pages.loginpag import LoginPage
from pages.addshop import AddShop
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from model.browser import browser_chrome


class SearchShop(BasePage):
    _url = BasePage._url + "/upload/admin/index.php"
    search_locator = (By.CSS_SELECTOR, "body > div.form-div > form > input[type=text]:nth-child(6)")  # 搜索输入框定位器
    search_button_locator = (By.CSS_SELECTOR, "body > div.form-div > form > input.button")  # 搜索按钮
    # driver = browser_chrome()
    def search_element(self):
        """
        获取搜索输入框元素
        :return:
        """
        return self.findelement(self.search_locator)

    def search_button_element(self):
        """
        获取搜索按钮元素
        :return:
        """
        return self.findelement(self.search_button_locator)

    def searshop(self):
        # lp = LoginPage(self.driver)
        # self.open()
        # lp.input_username("nichao")
        # lp.input_password("admin123")
        # lp.input_submit()
        # sleep(1)
        # ap=AddShop(self.driver)
        # ap.addshop()
        self.search_element().send_keys("森林公园")
        sleep(2)
        self.search_button_element().click()
        sleep(6)
