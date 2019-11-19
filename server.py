# coding: utf-8
import tkinter as tk
import time
import zmq

enter_count = 0
all_count = 0
def set_label():
    global enter_count
    global all_count

    message = socket.recv()
    if message==b"enter":
        enter_count+=1
        all_count+=1
    elif message==b"other_key":
        all_count+=1
    socket.send(b"Message Received")
    label_string = "Enter: "+str(enter_count)+'\n All: '+str(all_count)
    label['text'] = label_string
    root.after(10, set_label)


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")



root = tk.Tk()
label = tk.Label(root, text="placeholder")
label.pack()

set_label()
root.mainloop()