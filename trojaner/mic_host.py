#!/usr/bin/env python

import pyaudio
import socket
import select


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096
HOST = "192.168.2.100"
PORT = 8080

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST,PORT))
print("Listening for a connection...")
serversocket.listen(1)
conn, addr = serversocket.accept()




try:
    while True:
        data = conn.recv(CHUNK)
        stream.write(data)
except KeyboardInterrupt:
    pass

print('Shutting down')
s.close()
stream.close()
audio.terminate()

