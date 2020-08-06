#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  # 发送附件时使用
from email.mime.image import MIMEImage  # 发送图片附件时使用 ESVXSOOIEHFZCVTU
import sys
class SendEmail():
    def __init__(self):
        # 第三方 SMTP 邮件代理服务器的服务
        #使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）
        self.mail_host = "smtp.163.com"  # 设置服务器
        self.mail_user = "zhuswabc@163.com"  # 用户名
        self.mail_pass = "ESVXSOOIEHFZCVTU"  # 口令
 
        # 设置邮件的发件方和收件人列表
        self.sender = 'zhuswabc@163.com'  # 设置邮件发件方
        self.receivers = ['943614819@qq.com']  # 接收邮件列表，设置多个形如-- self.receivers = ['user1@126.com','user1@qq.com']
        pass
    #初始化登录信息，连接邮件服务器，并发送邮件
    def login_smtp_server_and_send(self,send_content):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, send_content.as_string())
            self['From'] = sender  #之前没有写From和To,发送邮件出现554错误
            self['To'] = receiver

            print ("邮件发送成功")
        except smtplib.SMTPException:
            print ("Error: 无法发送邮件,原因如下")
            info=sys.exc_info()
            print (info)
            print (info[0])
            print (info[1])
    # 邮件正文是文字或者html
    def send_words_content(self):
        mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.baidu.com">这是一个链接</a></p>
        <p align="center">成绩表</p>
        <table border="2px" align="center" bordercolor="blue" width="600px" height="300px">
        <tr align="center">
        <td>项目</td>
        <td colspan="5" >上课</td>
        <td colspan="2" >休息</td>
        </tr>
        <tr align="center">
        <td>星期</td>
        <td>星期一</td>
        <td>星期二</td>
        <td>星期三</td>
        <td>星期四</td>
        <td>星期五</td>
        <td>星期六</td>
        <td>星期日</td>
        </tr>
        <tr align="center">
        <td rowspan="4">上午</td>
        <td>语文</td>
        <td>数学</td>
        <td>英语</td>
        <td>英语</td>
        <td>物理</td>
        <td>计算机</td>
        <td rowspan="4">休息</td>
        </tr>
        <tr align="center">
        <td>数学</td>
        <td>数学</td>
        <td>地理</td>
        <td>历史</td>
        <td>化学</td>
        <td>计算机</td>
        <tr align="center">
        <td>政治</td>
        <td>英语</td>
        <td>体育</td>
        <td>历史</td>
        <td>地理</td>
        <td>计算机</td>
        </tr>  
        <tr align="center">
        <td>数学</td>
        <td>数学</td>
        <td>地理</td>
        <td>历史</td>
        <td>化学</td>
        <td>计算机</td>
        </tr>
        </table>
        """
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From'] = Header("发送文本", 'utf-8')
        message['To'] = Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试--正文为文本或html标签'
        message['Subject'] = Header(subject, 'utf-8')
        # 登录并发送邮件
        self.login_smtp_server_and_send(send_content=message)
        return
    # # 发送邮件带文件附件的例子
    # def send_attachmentfile_content(self):
    #     # 创建一个带附件的实例
    #     message = MIMEMultipart()
    #     message['From'] = Header("发送邮件带附件", 'utf-8')
    #     message['To'] = Header("测试", 'utf-8')
    #     subject = 'Python SMTP 邮件测试-带文件附件'
    #     message['Subject'] = Header(subject, 'utf-8')
 
    #     # 邮件正文内容
    #     message.attach(MIMEText('Python SMTP 邮件测试-带文件附件 的测试……', 'plain', 'utf-8'))
 
    #     # 构造附件1，传送当前目录下的 test.log 文件
    #     att1 = MIMEText(open('test.log', 'rb').read(), 'base64', 'utf-8')
    #     att1["Content-Type"] = 'application/octet-stream'
    #     # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    #     att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    #     message.attach(att1)
 
    #     # 构造附件2，传送当前目录下的 runoob.txt 文件
    #     att2 = MIMEText(open('use_common.py', 'rb').read(), 'base64', 'utf-8')
    #     att2["Content-Type"] = 'application/octet-stream'
    #     att2["Content-Disposition"] = 'attachment; filename="use_common.txt"'
    #     message.attach(att2)
    #     # 登录并发送邮件
    #     self.login_smtp_server_and_send(send_content=message)
    #     return
    # # 发送邮件时附件为图片的例子
    # def send_photo_attachment(self):
    #     msgRoot = MIMEMultipart('related')
    #     msgRoot['From'] = Header("发送邮件-附件为图片", 'utf-8')
    #     msgRoot['To'] = Header("测试", 'utf-8')
    #     subject = 'Python SMTP 邮件测试--附件为图片'
    #     msgRoot['Subject'] = Header(subject, 'utf-8')
 
    #     msgAlternative = MIMEMultipart('alternative')
    #     msgRoot.attach(msgAlternative)
 
    #     mail_msg = """
    #     <p>Python 邮件发送测试...</p>
    #     <p><a href="http://www.baidu.com">this is a url_link</a></p>
    #     <p>图片演示：</p>
    #     <p><img src="psb.jpeg"></p>
    #     """
    #     msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
    #     # 指定图片为当前目录
    #     fp = open('psb.jpeg', 'rb')
    #     msgImage = MIMEImage(fp.read())
    #     fp.close()
 
    #     # 定义图片 ID，在 HTML 文本中引用
    #     msgImage.add_header('Content-ID', '<image1>')
    #     msgRoot.attach(msgImage)
    #     # 登录并发送邮件
    #     self.login_smtp_server_and_send(send_content=msgRoot)
    #     return
# 创建对象，并一一调用各函数
obj_send_email=SendEmail()
obj_send_email.send_words_content()
# obj_send_email.send_attachmentfile_content()
# obj_send_email.send_photo_attachment()
