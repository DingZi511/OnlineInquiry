"""
===================================
Author:商汤科技-刘孜煜
Time：2023/8/22
E-mail:liuziyu1@senseauto.com
Company:商汤科技
===================================
"""
import jsonpath
import json
import unittest
import os
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from common.myconfig import conf
from common.handle_request import HandleRequest

file_path = os.path.join(DATA_DIR, "apicases.xlsx")
@ddt
class TestGenerate(unittest.TestCase):
    excel = ReadExcel(file_path, "generate_json")
    cases = excel.read_data()
    http = HandleRequest()

    @data(*cases)
    def test_generate(self, case):
        # 第一步：准备用例数据
        # 获取url
        url = conf.get_str("env", "url") + case["url"]
        # 获取数据
        # data = {
        #          "action": "To user",
        #          "gen_kwargs": {
        #          "model": "pjllama13bv7",
        #          "num_return_sequences": 1},
        #          "parent_messages": [
        #                               {"action": "From user",
        #                                "content": "假设你是一位经验丰富并且非常谨慎的的医生，会通过和患者进行多次的问答来明确自己的猜测，并且每次只能提一个问题，最终只会推荐相应的检验、检 查、就诊科室以及疑似的诊断，请回复患者的提问：我肚子疼"} ]
        #         }
        data = eval(case["data"])
        method = case["method"]
        headers = eval(conf.get_str("env", "headers"))
        # 该用例在表单的中所在行
        row = case["case_id"] + 1
        response = self.http.send(url=url, method=method, json=data, headers=headers)
        result_data = response.json()
        print(result_data)
        # 预期结果
        expected = case["expected"]
        string_expected = json.loads(expected)
        print("这是个很期待的值哇{}".format(string_expected))
        #提取返回数据到表格中去
        content_parts = jsonpath.jsonpath(result_data, "$..parts")[0]
        print(content_parts[0])
        self.excel.write_data(row=row,column=8,value=content_parts[0])
        # -------第三步：比对预期结果和实际结果-----
        try:
            # 业务码断言
            #self.assertEqual(expected["conversation_id"], result_data["conversation_id"])
            # msg断言
            self.assertEqual((string_expected["error"]), result_data["error"])
        except AssertionError as e:
            # excel中回写结果
            self.excel.write_data(row=row, column=9, value="未通过")

            # 报告中打印预期和实际结果
            print("预取结果：{}".format(string_expected))
            print("实际结果：{}".format(result_data))
            raise e
        else:
            # excel中回写结果
            self.excel.write_data(row=row, column=9, value="通过")






# if __name__ == '__main__':
#     unittest.main()
















