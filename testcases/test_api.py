"""
coding:utf-8
@File ：demo4.py
@Author ：shanren
@Date ：2022/10/20 17:41
"""
import re

import pytest
import requests
import jsonpath

# https://developers.weixin.qq.com/doc/offiaccount/User_Management/User_Tag_Management.html
from commons.yaml_util import write_yaml, read_yaml, read_yaml_testcase


class TestApi:
    # access_token = ""
    csrf_token = ""
    session = requests.session()

    # @classmethod
    # def setup(cls):
    #     print('每个用例之前的操作')
    #
    # @classmethod
    # def teardown(cls):
    #     print('每个用例之后的操作')
    #
    # @classmethod
    # def setup_class(cls):
    #     print('每个类之前的操作')
    #
    # @classmethod
    # def teardown_class(cls):
    #     print('每个类之后的操作')

    # 　获取access_token鉴权码接口
    @pytest.mark.parametrize('case', read_yaml_testcase('data/test_get_token.yaml'))
    def test_get_token(self, case):
        # url = 'https://api.weixin.qq.com/cgi-bin/token'
        # data = {"grant_type": "client_credential",
        #         "appid": "wx8a9de038e93f77ab",
        #         "secret": "8326fc915928dee3165720c910effb86"
        #         }
        url = case['request']['url']
        data = case['request']['params']
        res = requests.get(url=url, params=data)
        # lis = jsonpath.jsonpath(res.json(), '$.access_token')
        # print(lis[0])
        # token = res.json()['access_token']
        # print(token)
        # TestApi.access_token = res.json()['access_token']
        # print(TestApi.access_token)
        write_yaml({'access_token': res.json()['access_token']})

    # 编辑标签接口
    @pytest.mark.parametrize('case', read_yaml_testcase('data/test_edit_flag.yaml'))
    def test_edit_flag(self, case):
        # url = 'https://api.weixin.qq.com/cgi-bin/tags/update'
        # data = {"access_token": read_yaml('access_token')}
        # json = {"tag": {"id": 134, "name": "广东人"}}
        url = case['request']['url']
        data = case['request']['params']
        data['access_token'] = read_yaml('access_token')
        json = case['request']['json']
        res = requests.post(url=url, params=data, json=json)
        print(res.json())

    # 查询标签接口
    @pytest.mark.parametrize('case', read_yaml_testcase('data/test_select_flag.yaml'))
    def test_select_flag(self, base_url, case):
        # url = base_url + '/cgi-bin/tags/get'
        # data = {"access_token": read_yaml('access_token')}
        url = base_url + case['request']['url']
        data = case['request']['params']
        data['access_token'] = read_yaml('access_token')
        requests.get(url=url, params=data)

    # # 文件上传接口
    @pytest.mark.parametrize('case', read_yaml_testcase('data/test_file_upload.yaml'))
    def test_file_upload(self, case):
        # url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg'
        # data = {"access_token": read_yaml('access_token')}
        # file = {"media": open(r'C:\Users\zeng\Pictures\Default.jpg', 'rb')}
        url = case['request']['url']
        data = case['request']['params']
        data['access_token'] = read_yaml('access_token')
        file = case['request']['files']
        for key, value in file.items():
            file[key] = open(value, 'rb')
        res = requests.post(url=url, params=data, files=file)
        print(res.json())

    # # 访问phpwind首页接口
    # def test_phpwind(self):
    #     url = 'http://47.107.116.139/phpwind/'
    #     res = TestApi.session.request('get', url=url)
    #     # TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"/', res.text).group(1)
    #     # print(TestApi.csrf_token)
    #     write_yaml({'csrf_token': re.search('name="csrf_token" value="(.*?)"/', res.text).group(1)})
    #
    # # 登录接口
    # def test_login(self):
    #     url = 'http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
    #     header = {"Accept": "application/json, text/javascript, /; q=0.01",
    #               "X-Requested-With": "XMLHttpRequest"
    #               }
    #     data = {
    #         "username": "baili",
    #         "password": "baili123",
    #         "csrf_token": read_yaml('csrf_token'),
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     res = TestApi.session.request('post', url=url, headers=header, data=data)
    #     print(res.json())


if __name__ == '__main__':
    TestApi().test_get_token()
    TestApi().test_select_flag()
    TestApi().test_edit_flag()
    TestApi().test_file_upload()
    TestApi().test_phpwind()
    TestApi().test_login()
