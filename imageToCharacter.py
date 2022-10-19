import numpy as np
from PIL import Image
import sys
import json

args = sys.argv[1:]

filePath = args[0]
img      = Image.open(filePath).convert('RGBA')

imgW     = img.width
imgH     = img.height

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

px = np.array(img)
colorArr = []
for i in range(imgH):
    for j in range(imgW):
        if not(list(px[i][j])[3] == 0):
            x = list(px[i][j][:3])
            colorArr.append(rgb2hex(x[0], x[1], x[2]))
        else:
            colorArr.append("0")

""" for i in range(imgW * imgH):
    if not(px[i][3] == 0):
        x = list(px[i][:3])
        colorArr.append(rgb2hex(x[0], x[1], x[2])) """

px       = img.load()
pxArr    = []
objArr   = []

obj      = {"val": "#", "pos": [0,0], "z":1, "tag": "", "color": "#0000FF"}

if(args[1] == "std"):
    img      = img.convert("L")
    px       = img.load()

    low      = "#"
    low2     = "`"
    mid      = "I"
    mid2     = "⏺"
    high     = "W"
    high2    = "/"

    for i in range(imgW):
        for j in range(imgH):
            ind = (i * imgW) + j
            _px = px[i,j]
            if(px[i,j] <= 42 and px[i,j] != 0):
                tObj = obj
                tObj["pos"] = [i,j]
                tObj["val"] = low
                objArr.append(str(tObj))
            elif(px[i,j] <= 85 and px[i,j] != 0):
                tObj = obj
                tObj["pos"] = [i,j]
                tObj["val"] = low2
                objArr.append(str(tObj))
            elif(px[i,j] <= 120 and px[i,j] != 0):
                tObj = obj
                tObj["pos"] = [i,j]
                tObj["val"] = mid
                objArr.append(str(tObj))
            elif(px[i,j] <= 180 and px[i,j] != 0):
                tObj = obj
                tObj["pos"] = [i,j]
                tObj["val"] = mid2
                objArr.append(str(tObj))
            elif(px[i,j] <= 210 and px[i,j] != 0):
                tObj = obj
                tObj["pos"] = [i,j]
                tObj["val"] = high
                objArr.append(str(tObj))
else:
    for x in range(imgW):
        for y in range(imgH):
            if(y == 0): ind = x
            else: ind = (y * imgW) + x
            if not(colorArr[ind] == "0"):
                tObj = obj
                tObj["pos"] = [x,y]
                tObj["val"] = "█"
                tObj["color"] = colorArr[ind]
                objArr.append(str(tObj))

print("\n".join(objArr).replace("'",'"'))
