# input of 5 subjects marks
hin=int(input("Enter marks of hindi:"))
eng=int(input("Enter marks of english:"))
maths=int(input("Enter marks of maths:"))
sci=int(input("Enter marks of science:"))
san=int(input("Enter marks of sanscrit:"))
count=0
if hin<33:
   count=count+1
if eng<33:
   count=count+1
if maths<33:
   count=count+1
if sci<33:
   count=count+1
if san<33:
   count=count+1

print("no.of subjects having <33",count)
if count==0:
    print("pass") 
elif count<3:
    print("Supplementry")
else:
    print("fail")


