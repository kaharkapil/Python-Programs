import csv
with open("friends.csv",'r') as csvfile:
   rdr=csv.reader(csvfile)
   for row in rdr:
     print(row)
     print(row[3])
     print(row[4]*3)
#new program with file open
#like file handling in c language  
file=open("kap2.txt",'r')
print(file.read())
