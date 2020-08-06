import smtplib
from email.mime.text import MIMEText
from email.header import Header

#定义邮箱参数
mail_sever = 'smtp.163.com'        #邮箱服务器地址
mail_user = 'zhuswabc@163.com'          #邮箱用户名
mail_pass = 'ESVXSOOIEHFZCVTU'           #授权码

sender = 'zhuswabc@163.com'             #邮件发送方
reciver = '943614819@qq.com'             #邮件接收方

subject = 'python'                 #邮件标题
content = 'test'                   #邮件内容

#配置发送内容
msg = MIMEText(content,_subtype='plain',_charset='utf-8')  # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
msg['subject'] = Header(subject,'utf-8')        #邮件标题
msg['From'] = sender                            #邮件发送方
msg['To'] = reciver                            #邮件接收方

#实例化邮箱
smtp = smtplib.SMTP()                                #实例化邮箱
smtp.connect(mail_sever)                             #连接邮箱服务器
smtp.login(user=mail_user,password=mail_pass)        #登陆邮箱
smtp.sendmail(sender,reciver,msg.as_string())        #发送邮件
print('发送成功')