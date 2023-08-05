from mcpi import block
import math
import random
import sys
sys.path.insert(0, '')

from utils.startPoint import *

sp = getStartPoint()

vangle = 70
hangle = 45
for _ in range(20):
    dy = math.sin(math.radians(vangle))
    dx = math.cos(math.radians(vangle)) 
    dz = math.cos(math.radians(hangle)) 
    sp['x'] += dx 
    sp['z'] += dz 
    sp['y'] += dy
    mc.setBlock(sp['x'],sp['y'],sp['z'],block.WOOD.id)