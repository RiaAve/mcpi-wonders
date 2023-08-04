from mcpi import block
import random
import sys

sys.path.insert(0, '')

from utils.startPoint import *
    
sp = getStartPoint()

for n in range(0,100):
    dx = random.randint(-1, 1)
    dz = random.randint(-1, 1)
    sp['x'] = sp['x'] + dx
    sp['z'] = sp['z'] + dz
    woolType= random.randint(0,15)
    mc.setBlocks(sp['x'], sp['y'] + n, sp['z'],sp['x'] + 4, sp['y'] + n, sp['z'] + 4,block.WOOL.id, woolType)