import csv
name=input("enter name")
email=input("enter eamil")
with open('wrtefile.csv','w') as csvfile:
 fieldnames=['first_name','email']
 writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
 writer.writeheader()
 writer.writerow({'first_name':'kapil','email':'a@aa.com'})
 writer.writerow({'first_name':'rana','email':'a@aa.com'})
 writer.writerow({'first_name':'tina','email':'a@aa.com'})
 writer.writerow({'first_name':name,'email':email})
