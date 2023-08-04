from mcpi import block
import math
import sys

sys.path.insert(0, '')

from utils.startPoint import *
sp = getStartPoint()

for layer in range(20):
    for side in range(3):
        angle = side * 120 + 15
        for blockNumber in range(20 - layer):
            if blockNumber > layer:
                dx = math.cos(math.radians(angle)) 
                dz = math.sin(math.radians(angle)) 
                sp['x'] += dx
                sp['z'] += dz
                mc.setBlock(sp['x'], sp["y"], sp['z'], block.GRASS.id)
    sp['y'] += 1
    startdx = math.cos(math.radians(45)) 
    startdz = math.sin(math.radians(45)) 
    sp['x'] += startdx
    sp['z'] += startdz    
    
