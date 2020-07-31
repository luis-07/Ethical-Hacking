import pyaudio
import socket
import sys
import time
import select


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096
PORT = 8082
#HOST = "84.139.242.250"
HOST = "192.168.2.100"


time.sleep(1)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect((HOST, PORT))
audio = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    for s in read_list[1:]:
        s.send(in_data)
    return (None, pyaudio.paContinue)


# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)
# stream.start_stream()

read_list = [serversocket]


try:
    while True:
        readable, writable, errored = select.select(read_list, [], [])
        for s in readable:
            if s is serversocket:
                (clientsocket, address) = serversocket.accept()
                read_list.append(clientsocket)
                print("Client connected")
                
            else:
                data = s.recv(1024)
                if not data:
                    read_list.remove(s)
except KeyboardInterrupt:
    pass




serversocket.close()
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()




