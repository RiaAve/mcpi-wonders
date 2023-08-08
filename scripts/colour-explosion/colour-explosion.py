from mcpi import block
import random
import sys
sys.path.insert(0, '')

from utils.leaningLine import leaning_line
from utils.startPoint import getStartPoint

for _ in range(50):
    vangle = random.randint(1, 179)
    hangle = random.randint(1, 179)
    sp = getStartPoint()
    material = block.WOOL.id, random.randint(0,15)
    leaning_line(vangle, hangle, material, sp)