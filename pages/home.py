# -*- coding: utf-8 -*-
# @Time : 2020/12/10 21:53
# @Author : nichao
# @Email : 530504026@qq.com
# @File : home.py
# @Project : page
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class HomePage(BasePage):
    _url = BasePage._url + "/upload/admin/index.php"
    marketing_locator = (By.CSS_SELECTOR, "#submenu-div > ul > li:nth-child(1) > a > span")
    membermanagement_locator = (By.CSS_SELECTOR, "#menu-ul > li.collapse.lis.ico_7")  # 会员管理
    addmember_locator = (By.LINK_TEXT, "添加会员")  # 添加会员
    membername_locator = (By.NAME, "username")  # 会员名称
    emaill_locator = (By.NAME, "email")  # 邮箱
    password_locator = (By.NAME, "password")  # 密码
    confirm_password_locator = (By.NAME, "confirm_password")  # 确认密码
    confirm_button_locator = (By.CSS_SELECTOR, "body > div.main-div > form >"
                                               " table > tbody > tr:nth-child(14) > td > input:nth-child(1)")  # 添加会员确定按钮
    writemember_locator = (By.CSS_SELECTOR, "#listDiv > table > tbody > "
                                            "tr:nth-child(3) > td:nth-child(10) > a:nth-child(1)")  # 编辑按钮
    writemember_confirm_locator = (By.CSS_SELECTOR, "body > div.main-div > "
                                                    "form > table > tbody > tr:nth-child(18) > td > input:nth-child(1)")  # 编辑确定按钮
    keyword_locator = (By.CSS_SELECTOR, "body > div.form-div > form > input[type=text]:nth-child(5)")  # 关键字输入框
    selectbutton_locator = (By.CSS_SELECTOR, "body > div.form-div > form > input[type=submit]:nth-child(6)")  # [搜索按钮]
    member_strop_locator = (By.CSS_SELECTOR, "#listDiv > table > tbody > "
                                             "tr:nth-child(3) > td:nth-child(10) > a:nth-child(5)")  # 删除按钮
    assert_locator = (By.CSS_SELECTOR, "#listDiv > table > tbody")  # 断言使用的表tbody
    tr_locator = (By.TAG_NAME, "tr")
    td_locator = (By.TAG_NAME, "td")

    # tr_list=elememt.find_elements(*tr_locator)[2:]
    def sssert(self, assert_value):
        """
        断言
        :param assert_value:
        :return:
        """
        elememt = self.findelement(self.assert_locator)
        tr_list = self.findelements(self.tr_locator, self.findelement(self.assert_locator))[2:]
        for tr in tr_list:
            td_list = self.findelements(self.td_locator, tr)
            if td_list[1].text == assert_value:
                return td_list[1].text
            else:
                return "无"

    def find_value(self):  # 登录的断言
        return self.findelement(self.marketing_locator).text

    def membermanagement_element(self):
        """
        获取【会员管理】元素
        :return:
        """
        return self.findelement(self.membermanagement_locator)

    def addmember_element(self):
        """
        获取【添加会员】元素
        :return:
        """
        return self.findelement(self.addmember_locator)

    def membername_elemment(self):
        """
        获取【会员名称】元素
        :return:
        """
        return self.findelement(self.membername_locator)

    def membernameemail_element(self):
        """
        获取添加邮会员邮箱元素
        :return:
        """
        return self.findelement(self.emaill_locator)

    def password_elememt(self):
        """
        获取输入密码框元素
        :return:
        """
        return self.findelement(self.password_locator)

    def confirm_password_element(self):
        """
        获取确认密码框元素
        :return:
        """
        return self.findelement(self.confirm_password_locator)

    def confirmbutton_element(self):
        """
        获取添加会员确认按按钮元素
        :return:
        """
        return self.findelement(self.confirm_button_locator)

    def writemember_element(self):
        """
        获取编辑按钮元素
        :return:
        """
        return self.findelement(self.writemember_locator)

    def writememberconfirm_element(self):
        """
        获取编辑页面确认按钮元素
        :return:
        """
        return self.findelement(self.writemember_confirm_locator)

    def keyword_element(self):
        """
        获取输入关键字框元素
        :return:
        """
        return self.findelement(self.keyword_locator)

    def selectbutton_element(self):
        """
        获取搜索按钮元素
        :return:
        """
        return self.findelement(self.selectbutton_locator)

    def memberstrop_element(self):
        """
        获取删除按钮元素
        :return:
        """
        return self.findelement(self.member_strop_locator)

    def find_parentframe(self):
        """
        切换到上一级frame
        :return:
        """
        self.frame_parent()

    def find_appointframe(self, locator):
        """
        切换到指定的frame
        :param locator:
        :return:
        """
        self.switch_frame(locator)

    def confirm_dissmiss(self):
        """
        弹框取消
        :return:
        """
        self.driver.switch_to.alert.dismiss()

    def confirm_accept(self):
        """
        弹框确定
        :return:
        """
        self.driver.switch_to.alert.accept()

    def member(self, frame1, frame2, membername, memberemail, memberpassword, confirmpassword,
               writeemial, keyword):
        # hp = HomePage(self.driver)
        # bp=BasePage(self.driver)
        self.find_appointframe(frame1)
        sleep(2)
        self.membermanagement_element().click()  # 点击会员管理
        sleep(3)
        self.addmember_element().click()  # 点击添加会员
        sleep(1)
        self.find_parentframe()  # 切换到上一级frame
        self.find_appointframe(frame2)
        sleep(2)
        self.membername_elemment().send_keys(membername)  # 会员名称
        self.membernameemail_element().send_keys(memberemail)  # 邮箱地址
        self.password_elememt().send_keys(memberpassword)  # 密码
        self.confirm_password_element().send_keys(confirmpassword)  # 确认密码
        self.confirmbutton_element().click()  # 确定
        sleep(6)
        self.writemember_element().click()  # 点击【编辑】
        self.membernameemail_element().clear()
        self.membernameemail_element().send_keys(writeemial)  # 新邮箱地址
        sleep(4)
        self.writememberconfirm_element().click()  # 点击【确定】
        sleep(6)
        self.keyword_element().send_keys(keyword)  # 关键字
        self.selectbutton_element().click()  # 点击【搜索】
        sleep(3)
        self.memberstrop_element().click()  # 点击删除
        sleep(2)
        self.confirm_dissmiss()  # 取消
        sleep(2)
        self.memberstrop_element().click()  # 点击删除
        sleep(2)
        self.confirm_accept()  # 确定
        sleep(3)
