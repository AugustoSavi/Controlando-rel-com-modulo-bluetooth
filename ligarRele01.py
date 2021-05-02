import bluetooth
bd_addr = "mac-adress-hc-05"
port = 1
class Application():
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    data = "Rele01:off"
    sock.send(data)

Application()