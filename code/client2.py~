import bluetooth

bd_addr = "98:4F:EE:04:3C:66"
port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

msg = raw_input("q to end ->: ")
while msg != "q":
    print "msg is ", msg
    sock.send(msg)
    print "msg sent"
    print sock.recv(1024)
    msg = raw_input("q to end ->: ")

sock.close()
