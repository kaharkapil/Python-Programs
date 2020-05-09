import smtplib
import csv
gmailaddress = 'sirtbhopalstudents@gmail.com'
gmailpassword = 'bhopal*1231!'
mailto=input("Enter receiver email address")
msg='HII'
mailServer=smtplib.SMTP('Smtp.gmail.com',587)
mailServer.starttls()
mailServer.login(gmailaddress,gmailpassword)
mailServer.sendmail(gmailaddress,mailto,msg)
print("\n SENT")
mailServer.quit()
