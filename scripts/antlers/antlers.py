import math
from mcpi import block
import sys
sys.path.insert(0, '')
from utils.startPoint import * 
sp = getStartPoint()

radius = 5

for _ in range(5): 
    radius += 5 
    sx = sp['x']
    sy = sp['y'] + radius
    for a in range(0,360):
        x = math.cos(math.radians(a)) * radius + sx
        y = math.sin(math.radians(a)) * radius + sy
    
        mc.setBlock(x,y,sp['z'],block.WOOL.id)
