"""
===================================
Author:商汤科技-刘孜煜
Time：2023/8/22
E-mail:liuziyu1@senseauto.com
Company:商汤科技
===================================
"""
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
import os
from common.contants import CASE_DIR, REPORT_DIR
# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二步加载用例到套件
loader = unittest.TestLoader()

print(suite.addTest(loader.discover(CASE_DIR)))


# 第三步：创建一个测试用例运行程序

report_path = os.path.join(REPORT_DIR, "report.html")

with open(report_path, "wb") as f:
    runner = HTMLTestRunner(stream=f,
                            title="在线问诊的接口测试报告",
                            description="测试报告的描述信息。。。。。",
                            tester="liuziyu1@senseauto.com"
                            )
    # 第一步：运行测试套件
    # runner.run(suite)


    ontest = runner.run(suite)
    print("============",ontest.success_count)