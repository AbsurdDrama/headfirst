# -*- coding=utf-8 -*-
import time
import smtplib

from email.mime.text import MIMEText


def send(des_email, email_content, email_subject):
    """
    # 邮件发送主方法
    :param des_email: 目标邮箱地址
    :param email_content: 邮件内容
    :param email_subject: 邮件主题
    :return:  JSON 数据
    """
    new_email = EmailNotify(des_email=des_email, email_content=email_content,
                            email_subject=email_subject)
    send_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    new_email.send_email()

    if new_email.result == 'Success':
        print(1000, new_email.server
              ,new_email.email_content, new_email.email_subject, new_email.des_email
              , new_email.result, send_datetime)
        return new_email.result
    else:
        return new_email.result


class EmailNotify(object):
    """ Email Notify Class"""

    def __init__(self, des_email, email_content, email_subject):
        """
        Email Class init 默认使用 zhwnl 邮件服务器
        :param des_email: 目标邮箱地址
        :param email_content: 邮件内容
        :param email_subject: 邮件主题
        """
        self.server = "smtp.zhwnl.cn"
        self.port = 25
        self.user = "zouyh"
        self.password = "525125"
        self.sender = "zouyh@zhwnl.cn"
        # server SMTP 服务器地址, port 服务器端口, user 服务器用户, password 服务器用户密码, sender 邮件发送邮箱

        self.des_email = des_email
        self.email_content = email_content
        self.email_subject = email_subject
        # des_email 目标邮箱,  email_content 内容, email_subject 邮件主题

        self.result = ""
        # result 邮件发送状态

    def update_gateway(self, server, port, user, password, sender):
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.sender = sender

    def update_send_user(self, sender):
        # 注意修改发送用户需要在 SMTP 服务器对应 sender 的权限
        self.sender = sender

    def send_email(self):
        """
        邮件发送方法
        :return: self.result 会被修改 邮件是否发送成功
        """
        message = MIMEText(self.email_content, 'plain', 'utf-8')
        message['From'] = self.sender
        message['To'] = self.des_email
        message['Subject'] = self.email_subject
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.server, 25)
            smtp.starttls()
            smtp.login(self.user, self.password)
            smtp.sendmail(self.sender, self.des_email, message.as_string())
            smtp.quit()

            self.result = 'Success'
        except smtplib.SMTPServerDisconnected:
            self.result = 'Connect Error'
        # except:
        #     捕获所有异常保证程序响应
        #     self.result = 'Failed'


if __name__ == "__main__":
    send(email_content="OK P4 Endpoint:node4.all.sensors.dmp.com Metric:cpu.busy Tags: all(#3): 80.28464>90 Note: "
                       "Max:3, Current:1 Timestamp:2018-01-03 10:49:00 http://127.0.0.1:8081/portal/template/view/3",
         email_subject="[P4][OK][node4.all.sensors.dmp.com][][ all(#3) cpu.busy 80.28464>90][O1 2018-01-03 10:49:00]",
         des_email="1258353051@qq.com")

