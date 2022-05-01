from sqlite3 import Time
import serial.tools.list_ports as port_list
import serial
import torch
import cv2
import urllib.request
import numpy as np

class ControlCar:

    def __init__(self):
        self.url = 'http://192.168.29.34/1600x1200.jpg'
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
                

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

            results = self.model(img)   

            df = results.pandas().xyxy[0]

            for item in df.iterrows():
                x1 = int(item[1]['xmin'])
                x2 = int(item[1]['xmax'])
                y1 = int(item[1]['ymin'])
                y2 = int(item[1]['ymax'])

                name = item[1]['name']

                img = cv2.rectangle(img, (x1,y1), (x2,y2), (0, 255, 0), 1)
                cv2.putText(img,name,(x1,y1-10) ,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0, 255, 0))
        
            cv2.imshow("muon_live",img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

        
           
if __name__ == "__main__":
    car = ControlCar()
    car.initialize("COM4")
    car.run()