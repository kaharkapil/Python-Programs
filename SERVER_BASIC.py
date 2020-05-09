import socket
s = socket.socket()
print("Socket successfully created")
port=12346

s.bind(('',port))

print("Socket binded to %s" %(port))
s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    c.close()
