from Scene import Scene
from GameObject import GameObject

import random
import coloring
import math
import keyboard
import time
import random
import os
#os.system('cls')

Scene1 = Scene(59, 29)
Scene1.worldChar = "█"
Scene1.colored = True
Scene1.tick = 0.1

global log
log = ""

# Init Player
GameObject.screenSize = [60,30]

player = GameObject("player", "╬")
playerObj = {"val": coloring.red("╬"), "pos":[30,15], "z":3, "tag": "player"}
player.insertFrame(playerObj)
player.pos = [30,15]
Scene1.gameObjects.append(player)

def movePlayer():
    if(keyboard.is_pressed("space")):
        player.translate_y(-3)

# Init CityBG
city = GameObject("background", "", True)

city.importFromFile("./city.txt")
city.syncPos()
Scene1.gameObjects.append(city)

# Init Pilar
pilar = GameObject("pilar", "I", True)

pilar.importFromFile("./pilar.txt")
pilar.pos = [54,0]
pilar.syncPos()
Scene1.gameObjects.append(pilar)

def randPilar():
    v = random.randint(-4, 2)
    if(pilar.pos[0] == 0):
        pilar.translate_y(v)

while True:
    player.translate_y(1)
    city.translate_x(-1)
    pilar.translate_x(-1)

    movePlayer()
    #randPilar()

    Scene1.dt_start()
    Scene1.resetFrame()
    Scene1.clearTerm()
    Scene1.render()
    Scene1.dt_end()

    print(log)

    time.sleep(Scene1.tick + Scene1.deltaTime)
