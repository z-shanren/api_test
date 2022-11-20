"""
coding:utf-8
@File ：demo.py
@Author ：shanren
@Date ：2022/10/21 16:05
"""
import requests


class RequestUtil:
    session = requests.Session()

    def send_request(self, **kwargs):
        res = RequestUtil.session.request(**kwargs)
        print(res.text)
        return res


if __name__ == '__main__':
    RequestUtil.send_request(url='https://www.baidu.com/')
