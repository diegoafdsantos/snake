import time, random
from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
white = (255, 255, 255)
clear = (0, 0, 0)

trail = [[3, 3]]
direction = [1, 0]
lenght = 1
applePos = [random.randint(0, 7), random.randint(0, 7)]

pixels = [clear] * 64

def setDirection(d):
    global direction

    if d ==0:
        direction = [0, -1]
    elif d == 1:
        direction = [1, 0]
    elif d == 2:
        direction = [0, 1]
    elif d == 3:
        direction = [-1, 0]

while True:
    pixels = [clear] * 64

    for event in sense.stick.get_events():
        if event.direction == "up":
            setDirection(0)
        if event.direction == "right":
            setDirection(1)
        if event.direction == "down":
            setDirection(2)
        if event.direction == "left":
            setDirection(3)

    trail.insert(0, [trail[0][0] + direction[0], trail[0][1] + direction[1]])

    if trail[0][0] < 0:
        trail[0][0] = 7
    if trail[0][1] < 0:
        trail[0][1] = 7
    if trail[0][0] > 7:
        trail[0][0] = 0
    if trail[0][1] > 7:
        trail[0][1] = 0

    if trail[0] == applePos:
        applePos = [0]
        while applePos == []:
            applePos in trail:
                applePos = []
        lenght += 1
    elif trail[0] in trail [1:]:
        lenght = 1
    else:
        while len(trail) > lenght:
            trail.pop()

    for pos in trail:
        pixels[pos[1] * 8 + pos[0]] = white
    pixels[applePos[1] * 8 + applePos[0]] = red
    sense.set_pixels(pixels)
    time.sleep(0.15)
    





