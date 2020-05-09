amount=float(input("Enter amount"))
if amount<1000:
    discount=amount*0.05
    print("discount:",discount)
else:
    discount=amount*0.1
    print("discount:",discount)

print("net:",amount-discount)

