"""
coding:utf-8
@File ：conftest.py
@Author ：shanren
@Date ：2022/9/8 22:29
"""
import pytest

# @pytest.fixture(scope='function', autouse=False, params=[['mysql', 'redis']], ids=['mr'], name='c')
# def conn(request):
#     print('连接数据库')
#     yield request.param
#     print('关闭数据库')
from commons.yaml_util import clear_yaml


@pytest.fixture(scope='session', autouse=True)
def conn(request):
    print('连接数据库')
    clear_yaml()
    yield
    print('关闭数据库')
