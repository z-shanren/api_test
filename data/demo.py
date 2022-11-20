"""
coding:utf-8
@File ：demo.py
@Author ：shanren
@Date ：2022/10/22 17:11
"""
import os

from commons.yaml_util import read_value_yaml

# data = read_yaml_testcase('test_get_token.yaml')
# print(data)
# print(os.getcwd() + '/' + 'test_get_token.yaml')
data = read_value_yaml('test_get_token.yaml')
for i in data:
    print(i['feature'])
