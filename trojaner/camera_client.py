import socket
import cv2
import base64
import numpy as np
import pickle 
import struct
import os
import threading

os.system("title client")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#HOST = "192.168.2.100"
HOST = "84.139.242.250"
PORT = 8081
streaming = True
s.connect((HOST, PORT))
cap = cv2.VideoCapture(0)

while True:
    try:
        ret, frame=cap.read()
        data = pickle.dumps(frame)
        message_size = struct.pack("L", len(data))
        s.send(message_size + data)
    except:
        break

cap.release()
time.sleep(100)
sys.exit()

    


