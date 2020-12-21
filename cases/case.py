# -*- coding: utf-8 -*-
# @Time : 2020/12/10 19:08
# @Author : nichao
# @Email : 530504026@qq.com
# @File : case.py
# @Project : page
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.loginpag import LoginPage
from pages.home import HomePage
import unittest
from pages.base_page import BasePage
from model.browser import browser_chrome
from datatool import logindata, addmember, write, search
from cases.basecase import BaseCase
from pages.addshop import AddShop
from pages.searchshop import SearchShop
from pages.check import Check
from pages.web import Assert


class MyTest(unittest.TestCase):
    # driver = browser_chrome()
    def setUp(self):
        self.driver = browser_chrome()
        # driver = browser_chrome()
        username = logindata()[0][0]
        password = logindata()[0][1]
        lg = LoginPage(self.driver)
        lg.open()
        lg.input_username(username)
        lg.input_password(password)
        lg.input_submit()
        sleep(2)

    def test_addmember(self):
        frame1, frame2, membername, memberemail, memberpassword, confirmpassword = addmember()[0]
        writeemial = write()[0]
        keyword = search()[0][0]
        excepte = search()[0][1]

        hp = HomePage(self.driver)
        hp.member(frame1, frame2, membername, memberemail, memberpassword, confirmpassword,
                  writeemial, keyword)
        sleep(4)
        actual = hp.sssert(membername)
        self.assertEqual(excepte, actual, msg="测试不通过")

    def test_1(self):
        AddShop(self.driver).addshop()
        sleep(6)
        SearchShop(self.driver).searshop()
        sleep(2)
        Check(self.driver).checkshop()
        sleep(2)
        window_1 = self.driver.current_window_handle  # 获取当前窗口
        windows = self.driver.window_handles  # 获得打开的所有的窗口句柄
        # 切换到最新的窗口
        for current_window in windows:
            if current_window != window_1:
                self.driver.switch_to.window(current_window)
        Assert(self.driver).websearch_element().send_keys("森林公园")
        sleep(2)
        Assert(self.driver).websearchbutton_element().click()
        sleep(3)
        actul = Assert(self.driver).assertion()
        sleep(2)
        excepte = "森林公园"
        self.assertEqual(excepte, actul, msg="添加失败")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
