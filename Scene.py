import subprocess, platform
import time
from yachalk import chalk
import os
os.system('cls')

class Scene:
    # DeltaTime
    t0        = 0
    t1        = 0
    deltaTime = 0

    def dt_start(self): self.t0 = time.time()
    def dt_end(self):
        self.t1 = time.time()
        self.deltaTime = self.t1 - self.t0
    
    screenX     = 0
    screenY     = 0

    gameObjects = []
    tick        = 0

    worldChar   = ""
    output      = ""

    def __init__(self, _sX, _sY, _gO = [], _tK = 0.1, _wC = " "):
        # VAR DEF #
        self.screenX        = _sX
        self.screenY        = _sY
        self.gameObjects    = _gO
        self.tick           = _tK
        self.worldChar      = _wC
        
        self.colored        = False
        # VAR DEF (END) #

        self.resetFrame()
    
    def resetFrame(self):
        if(self.colored == False):
            self.output = (self.worldChar * self.screenX + "\n") * self.screenY
        else:
            temp = []
            for j in range(self.screenY + 1):
                if(j > self.screenY):
                    temp.append("\n")
                    break
                t = []
                for i in range(self.screenX + 1):
                    t.append(self.worldChar)
                t.append("\n")
                temp.append(t)
            
            self.output = temp
    
    def getObjIndex(self, _tag):
        return next((index for (index, d) in enumerate(self.gameObjects) if d["tag"] == _tag), None)
    
    def translateObjects(self, _goArr):
        sortedObjs = sorted(_goArr, key=lambda x: x["z"])
        for obj in sortedObjs:
            _mr = obj["val"]
            _px = obj["pos"][0]
            _py = obj["pos"][1]

            if(self.colored):
                #print(pos-100)
                #print(self.output[pos-100])

                self.output[_py][_px] = _mr
            else:
                if(_py == 0): pos = _px
                else: pos = (_py * (self.screenX + 1)) + _px
                self.output = (self.output[:pos]) + _mr + self.output[pos + 1:]
    
    def clearTerm(self):
        if platform.system()=="Windows":
            subprocess.Popen("cls", shell=True).communicate()
        else:
            print("\033c", end="")
    
    def render(self):
        go_aio = []
        for i in self.gameObjects:
            for j in i.draw():
                go_aio.append(j)
        
        self.translateObjects(go_aio)
        if(self.colored == False):
            print(self.output)
        else:
            s = ""
            for k in self.output:
                for h in k:
                    s += h
            print(s)