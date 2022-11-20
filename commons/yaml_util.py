"""
coding:utf-8
@File ：yaml_util.py
@Author ：shanren
@Date ：2022/10/22 12:28
"""
import os
from pathlib import Path

import yaml


# 写入
def write_yaml(data):
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='a+') as f:
        yaml.dump(data, stream=f, allow_unicode=True)

# def write_yaml(yaml_path):
#     with open(yaml_path, encoding='utf-8', mode='a+') as f:
#         yaml.dump(yaml_path, stream=f, allow_unicode=True)


# 读取
def read_yaml(key):
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='r') as f:
        data = yaml.load(f, yaml.FullLoader)
        return data[key]


# 读取
def read_value_yaml(yaml_path, key=None):
    with open(yaml_path, mode='r') as f:
        data = yaml.load(f, yaml.FullLoader)
        if key is not None:
            return data[key]
        else:
            return data


def read_all_yaml(yaml_path):
    with open(yaml_path, mode='r') as f:
        data = yaml.load(f, yaml.FullLoader)
        return data


# 清除
def clear_yaml():
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='w') as f:
        f.truncate()


def read_yaml_testcase(yaml_path):
    with open(os.getcwd() + '/' + yaml_path, mode='r') as f:
        data = yaml.load(f, yaml.FullLoader)
        return data


if __name__ == '__main__':
    write_yaml({'name': 'zeng'})
    print(read_yaml('name'))
    clear_yaml()
    # print(os.getcwd())
    # print(os.path.dirname(__file__))
    # print(Path.cwd().parent)
