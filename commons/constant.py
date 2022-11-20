"""
coding:utf-8
@File ：constants.py
@Author ：shanren
@Date ：2022/6/16 20:47
"""
import os

# 获取项目路径
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# 测试用例执行文件所在路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")
# print(CASE_DIR)

# 测试数据所在路径
DATA_FILE = os.path.join(BASE_DIR, "data")
# print(DATA_FILE)

# log所在路径
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_INFO = os.path.join(LOG_DIR, "info.log")
LOG_ERROR = os.path.join(LOG_DIR, "error.log")

# 测试报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")  # 拼接路径，得到 reports
REPORT_JSON = os.path.join(REPORT_DIR, "allure_json")  # 得到 reports包下的 allure_json包
REPORT_HTML = os.path.join(REPORT_DIR, "allure_report")  # 得到 reports包下的 allure_report包
# print(REPORT_HTML, REPORT_JSON)
