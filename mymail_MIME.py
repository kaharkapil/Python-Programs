import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'sirtbhopalstudents@gmail.com'
toaddr = input("Email of receiver")
tosub = input("Email subject")
tomsg = input("Email message...")
msg = MIMEMultipart()
msg['from'] = fromaddr
msg['to'] = toaddr
msg['subject'] = tosub
body=tomsg

msg.attach(MIMEText(body,'plain'))
filename ="csv2xml.py" #file to be sent
attachment = open(filename,"rb")

p = MIMEBase('application','octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',"attachment;filename=%s"%filename)
msg.attach(p)
s=smtplib.SMTP('Smtp.gmail.com',587)
s.starttls()
s.login(fromaddr,"bhopal*1231!")
text=msg.as_string()
s.sendmail(fromaddr,toaddr,text)
s.quit()
print("\nSENT")
