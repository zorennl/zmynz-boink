from keyboard import read_key as rk
from time import sleep

all_frames = open('python\\babygame\\assets\\frames.txt', 'r')
frames = []

for line in all_frames:
    frames.append(line.split()[0])

a = input("ARE YOU READY (Y/N)"); a = a.lower()
cframe=0 #current_frame

while a == "y":
    print(frames[cframe])
    key = rk()
    if rk("a"):
        print("nice")
        if cframe > 6:
            cframe = 3
    cframe += 1
    sleep(.2)