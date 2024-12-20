all_frames = open('assets/frames', 'r')
frames = []

for line in all_frames:
    frames.append(line.split()[0])

a = input("ARE YOU READY (Y/N)"); a = a.lower()

while a == "y":
    print("- - - - - - - - - - - -(BABY)")
    x = input