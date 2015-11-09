import smtplib  
from email.mime.text import MIMEText  # 引入smtplib和MIMEText

host = 'smtp.163.com'  
port = 25  
sender = 'alexkh3@163.com'  
pwd = 'XXXXXX'  
receiver = 'zhangyanan2@tuniu.com' 
body = '<h1>Hi</h1><p>test</p>' 

msg = MIMEText(body, 'html') 
msg['subject'] = 'Hello world' 
msg['from'] = sender  
msg['to'] = receiver  

s = smtplib.SMTP(host, port)  
s.login(sender, pwd)  
s.sendmail(sender, receiver, msg.as_string())  

print 'over'  
