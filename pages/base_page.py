# -*- coding: utf-8 -*-
# @Time : 2020/12/11 15:21
# @Author : nichao
# @Email : 530504026@qq.com
# @File : base_page.py
# @Project : page
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    _url = "http://192.168.1.161"

    def __init__(self, driver, url=None):
        self.driver = driver
        if not url:
            url = self._url
        self.url = url
    def open(self):
        self.driver.get(self.url)
    def findelement(self,locator,element=None):
        """
        单个元素查找方法
        :param locator:
        :param element:
        :return:
        """
        if element and isinstance(element,WebElement):
            return element.find_elements(*locator)
        return self.driver.find_element(*locator)
    def findelements(self,locator,element=None):
        """
        多个元素存在方法
        :param locator:
        :param element:
        :return:
        """
        if element and isinstance(element,WebElement):
            return element.find_elements(*locator)
        return self.driver.find_elements(*locator)
    def frame_parent(self):
        """
        切换到上级frame
        :return:
        """
        self.driver.switch_to.parent_frame()
    def switch_frame(self,frame):
        """
        切换到指定的frame
        :param frame:
        :return:
        """
        return self.driver.switch_to.frame(frame)



