"""
coding:utf-8
@File ：test.py
@Author ：shanren
@Date ：2022/10/23 11:43
"""
from commons.requests_util import RequestUtil

RequestUtil().send_request(method='get', url='https://www.baidu.com/')
