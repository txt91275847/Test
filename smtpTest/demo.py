import smtplib
from email.mime.text import MIMEText
from email.header import Header

message = MIMEText('Hello Boy!')   # 邮件内容
message['From'] = Header('小爱')   # 邮件发送者名字
message['To'] = Header('小蓝枣')   # 邮件接收者名字
message['Subject'] = Header('来自异世界的一封信!')   # 邮件主题

try:
    mail = smtplib.SMTP()
    mail.connect("smtp.qq.com")   #
    mail.login("912758847@qq.com", "keoxjpsaonslbbce")
    mail.sendmail("912758847@qq.com", "2263119046@qq.com", message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
