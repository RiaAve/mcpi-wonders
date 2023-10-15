import math
from mcpi import block
import sys
sys.path.insert(0, '')
from utils.startPoint import * 
sp = getStartPoint()

mc.setBlocks(sp['x'], sp['y'], sp['z'], sp['x'], sp['y'] + 49, sp['z'], block.STONE.id)

sp['y'] += 50

def drawDisk(hangle):
    radius = 5 

    for _ in range(5): 
        for angle in range(0,360):
            if angle <= 45 or (angle >= 135 and angle <= 225) or angle >= 315:
                x = math.cos(math.radians(angle)) * radius + sp['x']
                y = math.sin(math.radians(angle)) * radius + sp['y']

                mc.setBlock(x,y,sp['z'],block.WOOL.id)

        radius += 5

drawDisk(45)