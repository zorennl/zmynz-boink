import time

a = open('/home/zmynz/vss/git-repo/zmynz-boink/python/assets/alphabet', 'r')
alphabet = []

for line in a:
    alphabet.append(line.split()[0])

for i in range(len(alphabet)):
    print(alphabet[i])
    time.sleep(.5)
