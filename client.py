# coding: utf-8

import zmq
from pynput.keyboard import Key,Listener

def on_press(key):
    if key == Key.enter: 
        socket.send(b"enter")
    else:
        socket.send(b"other_key")
    socket.recv()

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#监听键盘按键
with Listener(on_press=on_press) as listener:
    listener.join()
#停止监视
Listener.stop()