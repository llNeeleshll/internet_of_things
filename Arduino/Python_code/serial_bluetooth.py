from sqlite3 import Time
import serial.tools.list_ports as port_list
import serial
ports = list(port_list.comports())

for p in ports:
    print (p)

serialPort = None

try:
    serialPort = serial.Serial(
        port="COM4", baudrate=9600
    )
except TimeoutError as e:
    print("Opps")

while True:

    val = input()
    
    b_val = bytes(val, encoding="ascii")
    serialPort.write(b_val)

serialPort.close()

pass