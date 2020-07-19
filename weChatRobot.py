import itchat
import requests

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
            'key': '126e08436e3e408f91ef3feb9277daeb',  # Tuling Key，API的值
            'info': msg,  # 发出去的消息
            'userid': 'coreglass',  # 用户名
            }
    r = requests.post(apiUrl, data=data).json() # post请求
    return r.get('text')

@itchat.msg_register(itchat.content.TEXT)  # 用于接收来自朋友间的对话消息
def print_content(msg):
    return get_response(msg['Text'])

@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)  # 用于接收群里面的对话消息
def print_content(msg):
    return get_response(msg['Text'])
itchat.auto_login()  # 通过微信扫描二维码登录
itchat.run()
