from mcpi import block
import math
import random
import sys
sys.path.insert(0, '')

from utils.startPoint import *

sp = getStartPoint()

vangle = 20
hangle = 45
for _ in range(20):
    dy = math.sin(math.radians(vangle))
    hyp2 = math.cos(math.radians(vangle)) 
    dx = math.sin(math.radians(hangle)) * hyp2
    dz = math.cos(math.radians(hangle)) * hyp2
    sp['x'] += dx 
    sp['z'] += dz 
    sp['y'] += dy
    mc.setBlock(sp['x'],sp['y'],sp['z'],block.WOOD.id)