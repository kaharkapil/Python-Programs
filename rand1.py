import random
i=random.randrange(21,60)
print ("ypur no,is:",i)
if i<20:
    print("no.is less than 20")
    if i%3==0:
        print("no.is multiple of 3")
elif i==20:
    print("no.is exactly 20")
else:
    if i%2==1:
     print("no.is odd")
    else:
        print("that is twice",i/2,'_')
    print("no.is more than 20")
    
