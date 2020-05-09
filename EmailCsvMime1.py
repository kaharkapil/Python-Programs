import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'sirtbhopalstudents@gmail.com'
tosub = 'emailcsvmime'
tomsg = 'testing'
with open('ECM.csv','r') as f:
     rows=csv.reader(f)
     for row in rows:
         toaddr = row[0]           
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
         
         mailserver=smtplib.SMTP('Smtp.gmail.com',587)
         mailserver.starttls()
         mailserver.login(fromaddr,"bhopal*1231!")
         text=msg.as_string()
         mailserver.sendmail(fromaddr,toaddr,text)
         print("Email sent to",row[0])
mailserver.quit()

