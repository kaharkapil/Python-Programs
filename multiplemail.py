import smtplib
import csv
gmailaddress = 'sirtbhopalstudents@gmail.com'
gmailpassword = 'bhopal*1231!'
with open('dataemail.csv','r') as f: 
    rows=csv.reader(f)
    for row in rows:
        mailto=row[3]
        with open('email01.txt','r') as myfile:
            msg=myfile.read()
        mailServer=smtplib.SMTP('Smtp.gmail.com',587)
        mailServer.starttls()
        mailServer.login(gmailaddress,gmailpassword)
        mailServer.sendmail(gmailaddress,mailto,msg)
        print("mail sent to",row[3])
print("\n SENT")
mailServer.quit()
