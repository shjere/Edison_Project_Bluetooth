import bluetooth

bd_addr = "98:4F:EE:03:5B:7E"
port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

msg = raw_input("q to end ->: ")
while msg != "q":
    print "msg is ", msg
    sock.send(msg)
    print "msg sent"
    msg = raw_input("q to end ->: ")

sock.close()
