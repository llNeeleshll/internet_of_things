from sqlite3 import Time
import serial.tools.list_ports as port_list
import serial

serialPort = None

try:
    serialPort = serial.Serial(
        port="COM4", baudrate=9600
    )
except TimeoutError as e:
    print("Opps")

while True:

    val = input("Enter your message : ")

    val  = val + "#"
    
    b_val = bytes(val, encoding="ascii")

    serialPort.write(b_val)
    serialPort.flush()

    message = ""

    while True:
        line = serialPort.readline()

        line = line.decode("utf-8")

        if "#" in line:
            break

        message += line.strip() 

    print(message)

serialPort.close()

pass