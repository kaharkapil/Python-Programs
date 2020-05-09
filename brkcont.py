count =0
while True:
    print(count)
    count+=1
    if count>=5:
        break
print("-----------------------------------------------")
# prints odd number
for i in range(21):
    #check if i is even
    if i%2==0:
        continue
    print(i)
print("----------------------------------------------")
for i in range(21):
    #check if i is odd
    if i%2!=0:
        continue
    print(i)
print("----------------------------------------------")
for abc in "kapilkahar":
   if abc=='p' or abc=='h':
      break
   print("current",abc)
