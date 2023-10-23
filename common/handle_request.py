"""
===================================
Author:商汤科技-刘孜煜
Time：2023/8/22
E-mail:liuziyu1@senseauto.com
Company:商汤科技
===================================
"""
'''
发送post请求，，发送get请求，发送patch请求，
    代码中如何做到不同请求方式的接口去发送不同的请求
    加判断

'''
import requests

class HandleRequest:
    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法转换为小写
        method = method.lower()
        if method == "post":
            return requests.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return requests.patch(url=url, json=json, data=data, headers=headers)
        elif method == "get":
            return requests.get(url=url, params=params,headers=headers)


class HandleSessionRequest:
    """使用session鉴权的接口，使用这个类类发送请求"""

    def __init__(self):
        self.se = requests.session()

    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法转换为小写
        method = method.lower()
        if method == "post":
            return self.se.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return self.se.patch(url=url, json=json, data=data, headers=headers)
        elif method == "get":
            return self.se.get(url=url, params=params)


if __name__ == '__main__':
    # 登录接口地址
    generate_url = "https://mchatgpt-internal.dev.6ccloud.com/v1/api/completion/generate_json"

    # 登录的参数
    generate_data = {
	"action": "To user",
	"gen_kwargs": {
		"model": "pjllama13bv7",
		"num_return_sequences": 1},
	"parent_messages": [
	 {"action": "From user",
		"content": "假设你是一位经验丰富并且非常谨慎的的医生，会通过和患者进行多次的问答来明确自己的猜测，并且每次只能提一个问题，最终只会推荐相应的检验、检 查、就诊科室以及疑似的诊断，请回复患者的提问：我肚子疼"},
	 {"action": "To user",
		"content": "您好，很抱歉听到您有肚子疼的不适。我需要了解更多关于您的症状和病史，以便能够更好地帮助您。首先，您能否告诉我您的疼痛部位在哪里？"},
	 {"action": "From user",
		"content": "腹部疼痛"},
	 {"action": "To user",
		"content": "好的，谢谢您的回答。您能否告诉我您的疼痛是何时开始的？是突然开始还是逐渐加重的？"},
	 {"action": "From user",
		"content": "突然开始的"},
	 {"action": "To user",
		"content": "好的，谢谢您的回答。您是否有其他症状，例如恶心、呕吐、腹泻、发热等？"},
	 {"action": "From user",
		"content": "腹泻和发热"}
		                  ]
}
    # 登录的请求头
    header = {
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxZTNmOWNmOS0xY2FmLTQ1MWEtODQ5Ny05ZjFjNWJkMjFjNTUiLCJleHAiOjIwMDI1MTQ3NTksInNjb3BlcyI6WyJ1c2VyIl19.A63omA3BYGSwkRpYx6Ou4OzuvxmdLN7M69knCij_rQc",
        "content-type": "application/json; charset=utf-8"
    }

    http = HandleRequest()
    res = http.send(url=generate_url, method="post", json=generate_data, headers=header)
    print(res.json())

