from mcpi import block
import random
import sys
sys.path.insert(0, '')

from utils.leaningLine import leaning_line
from utils.startPoint import getStartPoint

vangle = 60
hangle = 30
sp = getStartPoint()
original_x = sp['x']

for _ in range(5):
    for _ in range(5):
        material = block.WOOL.id, random.randint(0,15)
        leaning_line(vangle, hangle, material, sp)
        sp['x'] += 1
    sp['x'] = original_x
    sp['z'] += 1