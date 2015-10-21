import bluetooth

bd_addr = "98:4F:EE:03:5B:7E"
port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

msg = "Hello!"
sock.send(msg)

sock.close()
