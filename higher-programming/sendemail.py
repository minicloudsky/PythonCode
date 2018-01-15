import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
# 接收邮件
receivers = ['1397991131@qq.com']
message = MIMEText('Python 邮件发送测试','plain','utf-8')
message['From'] = Header("菜鸟教程",'utf-8')
message['To'] = Header('测试','utf-8')
subject = 'Python SMTP邮件测试'
message['Subject'] = Header(subject,'utf-8')
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error: 无法发送邮件')