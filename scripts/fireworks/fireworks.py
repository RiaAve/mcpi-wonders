from mcpi import block
import random
import math
import sys
sys.path.insert(0, '')

from utils.startPoint import * 

def leaning_arc(vangle, hangle, material, original_sp):
    sp = original_sp.copy()
    numberOfBlocks = random.randint(35, 45)
    for _ in range(numberOfBlocks):
        dy = math.sin(math.radians(vangle))
        hyp2 = math.cos(math.radians(vangle)) 
        dx = math.sin(math.radians(hangle)) * hyp2
        dz = math.cos(math.radians(hangle)) * hyp2
        sp['x'] += dx 
        sp['z'] += dz
        sp['y'] += dy
        mc.setBlock(sp['x'], sp['y'], sp['z'], material)
        vangle -= 100 / numberOfBlocks

sp = getStartPoint()
material = block.GLASS.id 

leaning_arc(60, 50, material, sp)

