from mcpi import block
import math
import random
import sys
sys.path.insert(0, '')

from utils.startPoint import *

for _ in range(50):
    vangle = random.randint(1, 359)
    hangle = random.randint(1, 359)
    sp = getStartPoint()
    material = block.WOOL.id, random.randint(0,15)
    for _ in range(random.randint(15, 25)):
        dy = math.sin(math.radians(vangle))
        hyp2 = math.cos(math.radians(vangle)) 
        dx = math.sin(math.radians(hangle)) * hyp2
        dz = math.cos(math.radians(hangle)) * hyp2
        sp['x'] += dx 
        sp['z'] += dz
        sp['y'] += dy
        mc.setBlock(sp['x'], sp['y'], sp['z'], material)