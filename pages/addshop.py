# -*- coding: utf-8 -*-
# @Time : 2020/12/15 16:24
# @Author : nichao
# @Email : 530504026@qq.com
# @File : addshop.py
# @Project : page
from time import sleep

from selenium import webdriver
from pages.base_page import BasePage
from pages.home import HomePage
from model.browser import browser_chrome
from datatool import logindata
from pages.loginpag import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddShop(BasePage):
    _url = BasePage._url+"/upload/admin/index.php"
    goods_locator=(By.CSS_SELECTOR,"#menu-ul > li.collapse.lis.ico_1")#商品管理定位器
    addgoods_locator=(By.CSS_SELECTOR,"#menu-ul > li.explode.lis.ico2_1 > ul > li:nth-child(2) > a")#添加新商品定位器
    goods_name_locator=(By.NAME,"goods_name")#商品名称
    cat_id_locator=(By.NAME,"cat_id")#商品分类
    pitrute_locator=(By.CSS_SELECTOR,"#general-table > tbody > "
            "tr:nth-child(15) > td:nth-child(2) > input[type=file]:nth-child(1)")#上传图片定位器
    confirm_button_locator=(By.CSS_SELECTOR,"input[value=' 确定 ']")#添加商品确定按钮
    # check_locator = (By.CSS_SELECTOR,
    # "#listDiv > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(11) > a:nth-child(1) > img")  # 查看按钮
    # driver=browser_chrome()

    def goods_element(self):
        """
        获取商品管理元素
        :return:
        """
        return self.findelement(self.goods_locator)
    def addgoods_element(self):
        """
        获取添加商品元素
        :return:
        """
        return self.findelement(self.addgoods_locator)
    def goods_name_element(self):
        """
        获取输入商品名称的元素
        :return:
        """
        return self.findelement(self.goods_name_locator)
    def cat_id_element(self):
        """
        获取商品分类的元素
        :return:
        """
        return self.findelement(self.cat_id_locator)
    def pitrute_element(self):
        """
        获取上传图片的元素
        :return:
        """
        return self.findelement(self.pitrute_locator)
    def confirm_element(self):
        """
        获取添加商品[确定]按钮元素
        :return:
        """
        return self.findelement(self.confirm_button_locator)
    def addshop(self):
        # username = logindata()[0][0]
        # password = logindata()[0][1]
        # lg = LoginPage(self.driver)
        # lg.open()
        # lg.input_username(username)
        # lg.input_password(password)
        # lg.input_submit()
        # sleep(2)
        self.switch_frame("menu-frame")
        sleep(1)
        self.goods_element().click()
        sleep(1)
        self.addgoods_element().click()
        sleep(1)
        self.frame_parent()
        self.switch_frame("main-frame")
        self.goods_name_element().send_keys("森林公园")
        sleep(2)
        sele_element = self.cat_id_element()
        select = Select(sele_element)
        select.select_by_index(3)
        sleep(2)
        self.pitrute_element().send_keys(r"C:\Users\nichao\PycharmProjects\page\data\picture.jpg")  # 上传图片
        sleep(6)
        self.confirm_element().click()  # 点击确定
        sleep(1)

