from sqlite3 import Time
import serial.tools.list_ports as port_list
import serial
import keyboard
import cv2
import subprocess
import numpy as np

class ControlCar:

    def __init__(self):
        self.cmd_camera_vision = 'python display_image.py'
                

    def initialize_and_control(self, port):

        self.serialPort = None

        try:
            self.serialPort = serial.Serial(
                port=port, baudrate=9600
            )

            print("Muon is connected.")
            subprocess.call(" " + self.cmd_camera_vision, shell=True)
            
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
            elif(key == "q"):
                self.serialPort.close()
                print("Muon is disconnected")
                break
            else:
                continue
            
            b_val = bytes(val, encoding="ascii")

            self.serialPort.write(b_val)
            line = self.serialPort.readline()
           
if __name__ == "__main__":
    car = ControlCar()
    car.initialize_and_control("COM4")