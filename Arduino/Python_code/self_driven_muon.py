from sqlite3 import Time
import serial.tools.list_ports as port_list
import serial
import keyboard
import cv2
import urllib.request
import numpy as np

class ControlCar:

    def __init__(self):
        self.url = 'http://192.168.29.34/1600x1200.jpg'
                

    def initialize(self, port):

        self.serialPort = None

        try:
            self.serialPort = serial.Serial(
                port=port, baudrate=9600
            )

            print("Muon is connected.")
            
        except TimeoutError as e:
            print("Opps")

    def run(self):
        
        while True:

            try:
                img_resp=urllib.request.urlopen(self.url, timeout=5)
            except Exception as e:
                break

            imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
            img=cv2.imdecode(imgnp,-1)

            img = cv2.resize(img, (700,500))   
        
            cv2.imshow("muon_live",img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

        
           
if __name__ == "__main__":
    car = ControlCar()
    car.initialize("COM4")
    car.run()