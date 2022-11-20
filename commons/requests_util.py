"""
coding:utf-8
@File ：requests_util.py
@Author ：shanren
@Date ：2022/10/23 11:39
"""
import requests


class RequestUtil:
    session = requests.session()

    def send_request(self, method, url, **kwargs):
        res = RequestUtil.session.request(method, url, **kwargs)
        print(res.content.decode('utf-8'))
        return res
