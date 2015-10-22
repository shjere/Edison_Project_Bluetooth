import bluetooth

bd_addr = "98:4F:EE:04:3C:66"
port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

msg = "Hello from Shashank!"
sock.send(msg)

msg = sock.recv(1024)
print msg

sock.close()
