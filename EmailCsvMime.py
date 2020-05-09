import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'sirtbhopalstudents@gmail.com'
tosub = 'emailcsvmime'
tomsg = 'testing'
with open('dataemail.csv','r') as f:
     rows=csv.reader(f)
     for row in rows:
         toaddr = row[3]
         with open('email01.txt','r') as myfile:
              msg1=myfile.read()    #text file tob be sent
         msg = MIMEMultipart()      #instance of MIMEMultipart          
         msg['from'] = fromaddr     #storing the senders email address
         msg['to'] = toaddr         #storing the receivers email address
         msg['subject'] = tosub     #storing the subject

         body=tomsg                 #string to store the body of the mail
         msg.attach(MIMEText(body,'plain'))
         filename ="csv2xml.py"     #file to be attached
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
         mailserver.sendmail(fromaddr,toaddr,msg1)
         print("Email sent to",row[3])
mailserver.quit()

