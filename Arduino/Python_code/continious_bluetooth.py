from sqlite3 import Time
import serial.tools.list_ports as port_list
import serial
import keyboard

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

    val = 0

    key = keyboard.read_key()

    if(key == "0"):
        val = 0
    elif(key == "1"):
        val = 1
    
    b_val = bytes(key, encoding="ascii")

    serialPort.write(b_val)

serialPort.close()

pass