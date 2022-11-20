"""
coding:utf-8
@File ：run.py
@Author ：shanren
@Date ：2022/10/21 20:45
"""
import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system('allure generate ./temps -o ./reports --clean')
