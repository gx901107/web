# -*- coding: utf-8 -*-
# @Time : 2020/12/11 15:12
# @Author : nichao
# @Email : 530504026@qq.com
# @File : loginpag.py
# @Project : page
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    _url = BasePage._url + "/upload/admin"
    username_locator = (By.NAME, 'username')
    password_locator = (By.NAME, 'password')
    submit_locator = (By.CSS_SELECTOR, 'input[type="submit"]')

    # def open(self):
    #     self.driver.get(self.url)
    def input_username(self, username):
        element = self.findelement(self.username_locator)
        element.clear()
        element.send_keys(username)

    def input_password(self, password):
        pa_element = self.findelement(self.password_locator)
        pa_element.clear()
        pa_element.send_keys(password)

    def input_submit(self):
        self.findelement(self.submit_locator).click()
