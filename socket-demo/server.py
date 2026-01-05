import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(5)

print("Server waiting for connection...")

conn, addr = s.accept()
print("Connected with", addr)

conn.send(b"Hello Client")
conn.close()
