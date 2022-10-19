import coloring
import colorful
import json
from yachalk import chalk

class GameObject:
    screenSize = [0,0]

    def __init__(self, _n, _c, _t = False):
        self.name = _n
        self.char = _c
        self.tile = _t

        self.pos      = [0,0]
        self.sizeX    = 0
        self.sizeY    = 0

        self.frames   = []
        self.frame    = 0

    # {"val": "#", "pos":[20,5], "z":1, "tag": "player"}
    def insertFrame(self, _obj):
        ret = []
        _obj["tag"] = self.name
        _obj["pos"][0] += self.pos[0]
        _obj["pos"][1] += self.pos[1]
        ret.append(_obj)
        self.frames.append(ret)

    def draw(self):
        if(len(self.frames) > 0):
            self.updateFrame()
            return self.frames[self.frame]
        

    def updateFrame(self):
        if(self.frame == len(self.frames) - 1):
            self.frame = 0
        else:
            self.frame += 1

    def translate_x(self, _steps):
        for i in self.frames:
            for j in i:
                if(self.tile):
                    if((j["pos"][0] + _steps) < 0):
                        j["pos"][0] = self.screenSize[0] + _steps
                    else:
                        j["pos"][0] += _steps
                else:
                    j["pos"][0] += _steps

    def translate_y(self, _steps):
        for i in self.frames:
            for j in i:
                if(self.tile):
                    if(j["pos"][1] + _steps < 0):
                        j["pos"][1] = self.screenSize[1] + _steps
                    elif(j["pos"][1] + _steps > self.screenSize[1]):
                        j["pos"][1] = 0 + ((j["pos"][1] + _steps) - self.screenSize[1])
                    else:
                        j["pos"][1] += _steps
                else:
                    j["pos"][1] += _steps

    def translate(self):
        for i in self.frames:
            for j in i:
                j["pos"][0] = self.pos[0] - j["pos"][0]
                j["pos"][1] = self.pos[1] - j["pos"][1]

    def importFromFile(self, _path):
        _lines = []
        with open(_path, "r", encoding="utf-8") as f:
            _lines = f.readlines()

        ret = []
        for i in _lines:
            k = json.loads(i)
            k["tag"] = self.name
            k["pos"][0] += self.pos[0]
            k["pos"][1] += self.pos[1]
            ret.append(k)

        self.frames.append(ret)
        self.colorFrames()
    
    def colorFrames(self):
        for i in self.frames:
            for j in i:
                print(j)
                j["val"] = coloring.colorize(j["val"], j["color"])
                #print(j)

    def syncPos(self):
        mid = int(len(self.frames[self.frame]) / 2)
        self.pos = self.frames[self.frame][mid]["pos"]
        #self.frames[self.frame][mid]["val"] = "#"
