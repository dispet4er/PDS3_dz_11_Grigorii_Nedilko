import socket
from datetime import date
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    if data == b'hi':
        print(str(data))
        conn.send(bytes("hello", encoding='UTF-8'))
    elif data == b'what date is today':
        print(str(data))
        dateAsString = str(date.today())
        conn.send(dateAsString.encode())
    elif data == b'what time is now':
        print(str(data))
        timeAsString = str(datetime.now())
        conn.send(timeAsString.encode())
conn.close()