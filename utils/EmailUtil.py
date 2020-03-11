# -*- coding: utf-8 -*-
from  config.Conf_File import ConfigYaml
from  email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
import smtplib
class SendEmail:

    #初始化 smtp地址 用户名 密码    接收邮件的地址    邮件内容 邮件标题  邮件附件
    def __init__(self,smtp_addr,username,password,recv,title,content=None,file=None):
        # con = ConfigYaml().get_emil()
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file

    #发送邮件方法
    def send_mail(self):
        #处理邮件信息的类
        msg = MIMEMultipart()
        #插入邮件正文(邮件内容) 需要注意的是发送字符串内容要先转换成文本 设置指定的字符集
        msg.attach(MIMEText(self.content,_charset="utf-8"))
        #设置邮件头信息
        msg["Subject"] = self.title
        #设置用户名
        msg["From"] = self.username
        #设置邮件内容
        msg["To"] = self.recv
        #判断是否有附件
        if self.file:
            #读取附件内容
            att = MIMEText(open(self.file).read())
            #设置附件内容类型
            att["Content-Type"] = 'application/octet-stream'
            # att["Content-Type"] = 'application/octet-stream'
            #设置附件头
            att["Content-Disposition"] = 'attachment;filename="{}"'.format(self.file)
            #把内容加到邮件主题中
            msg.attach(att)

        #登录邮件服务器
        self.smtp = smtplib.SMTP(self.smtp_addr,port=25)
        self.smtp.login(self.username,self.password)
        #发送邮件
        self.smtp.sendmail(self.username,self.recv,msg.as_string())


if __name__ == "__main__":
    from  config.Conf_File import ConfigYaml
    email_info = ConfigYaml().get_emil()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(smtp_addr, username, password, recv, "我的邮件发送")
    email.send_mail()