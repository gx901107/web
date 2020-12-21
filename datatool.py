# -*- coding: utf-8 -*-
# @Time : 2020/12/11 19:27
# @Author : nichao
# @Email : 530504026@qq.com
# @File : datatool.py
# @Project : page
import xlrd
from config.configs import DATA_PATH
def logindata(filename= None):
    """
    取登录的参数
    :param filename:
    :return:
    """
    if not filename:
        filename=DATA_PATH
    data=xlrd.open_workbook(filename)
    table=data.sheet_by_name("login")
    data_list=[]
    for n_row in range(1,table.nrows):
        data_list.append(table.row_values(n_row))
    return data_list
print(logindata())
def addmember(filename=None):
    """
    添加会员的参数
    :param filename:
    :return:
    """
    if not filename:
        filename=DATA_PATH
    data=xlrd.open_workbook(filename)
    table=data.sheet_by_name("addmember")
    data_list=[]
    for n_row in range(1,table.nrows):
        data_list.append(table.row_values(n_row))
    return data_list
def write(filename=None):
    """
    会员编辑的参数
    :param filename:
    :return:
    """
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name("write")
    data_list = []
    for n_row in range(1, table.nrows):
        data_list.append(table.row_values(n_row))
    return data_list
def search(filename=None):
    """
    搜索的参数
    :param filename:
    :return:
    """
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name("search")
    data_list = []
    for n_row in range(1, table.nrows):
        data_list.append(table.row_values(n_row))
    return data_list

