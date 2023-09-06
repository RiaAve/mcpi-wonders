from mcpi import block
import random
import sys
sys.path.insert(0, '')

from utils.startPoint import * 
from utils.leaning_arc import * 

sp = getStartPoint()

for _ in range(100):
    vangle = random.randint(1, 359)
    hangle = random.randint(1, 359)
    material = block.WOOL.id, random.randint(0,15)
    leaning_arc(vangle, hangle, material, sp)

