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

    if(key == "up"):
        val = 'F'
    elif(key == "down"):
        val = 'B'
    elif(key == "right"):
        val = 'R'
    elif(key == "left"):
        val = 'L'
    elif(key == "s"):
        val = 'S'
    else:
        continue
    
    b_val = bytes(val, encoding="ascii")

    serialPort.write(b_val)
    line = serialPort.readline()
    # print(line)

serialPort.close()

pass