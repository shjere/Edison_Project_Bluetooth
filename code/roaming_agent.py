import bluetooth
import sys
import time
#import bluetooth.btcommon.* 

bd_addr = "98:4F:EE:03:5B:7E"
port = 0x1001

def connect_bluetooth():
    sock = None
    while sock is None:
        print "Attempting to establish connection..."
        try:
            sock = bluetooth.BluetoothSocket( bluetooth.L2CAP )
            sock.connect((bd_addr, port))
            print "Connection established"
            return sock
        except bluetooth.btcommon.BluetoothError as e:
            sock = None

def send_message(sock):
    msg = raw_input("q to end ->: ")
    while msg != "q":
        print "msg is ", msg
        sock.send(msg)
        print "msg sent"
        msg = raw_input("q to end ->: ")
    
    sys.exit()

def spam_anchor(sock):
    i = 0
    while True:
        sock.send("Hello {}".format(i))
        i+=1
        time.sleep(0.5)

if __name__ == "abcde":
    sock = connect_bluetooth()
    while True:
        try:
            send_message(sock)
        except bluetooth.btcommon.BluetoothError as e:
            new_sock = None
            while new_sock is None:
                print "trying to re-establish connection..."
                try:
                    new_sock = connect_bluetooth()
                except bluetooth.btcommon.BluetoothError as e:
                    new_sock = None

    sock.close()


if __name__ == "__main__":
    sock = connect_bluetooth()
    while True:
        try:
            spam_anchor(sock)
        except bluetooth.btcommon.BluetoothError as e:
            sock = connect_bluetooth()
    sock.close()
