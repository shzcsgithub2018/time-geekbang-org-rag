import json
import requests

def get_access_token():
  ernie_client_id = EOy6udGspndqBYQ82BunCVR5 # 替换为你的client_id
  ernie_client_secret = pCkCDamdQDr22Y0mtmUJ5d46k8A4ei08 # 替换为你的client_secret
  url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ernie_client_id}&client_secret={ernie_client_secret}"
  
  playload= json.dumps("")
  headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=playload)
  return response.json().get("access_token")

def 对话模式(messages):
  url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-lite-8k?access_token=" + get_access_token()
  
  json_obj = {
      "messages": messages,
  }

  playload= json.dumps(json_obj)
  headers = {
      'Content-Type': 'application/json'
  }
  
  response = requests.request("POST", url, headers=headers, data=playload)
  json_result = json.loads(response.text)
  return json_result["result"]

def 获取结构化数据查询参数(用户输入):
    结构化数据 = 对话模式(构造解析用户输入并返回结构化数据用的messages(用户输入))
    查询参数 = json.loads(结构化数据)
    return 查询参数

def 构造解析用户输入并返回结构化数据用的messages(用户输入):
  messages=[
  {"role": "user", "content": f"""
  请根据用户的输入返回json格式结果。注意，模块部分请按以下选项返回对应序号：
   1. 销售对账
   2. 报价单
   3. 销售订单
   4. 送货单
   5. 退货单
   6. 其他

  示例1：
  用户：客户北京极客邦有限公司的款项到账了多少？
  系统：
  {{'模块':1,'客户名称':'北京极客邦有限公司'}}

  示例2：
  用户：你好
  系统：
  {{'模块':6,'其他数据',None}}

  示例3：
  用户：最近一年你过得如何？
  系统：
  {{'模块':6,'其他数据',None}}

  用户：{用户输入}
  系统：
  """},
  ]
  return messages



