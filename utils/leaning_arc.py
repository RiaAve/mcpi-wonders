import math
import random
import sys
sys.path.insert(0, '')

from utils.startPoint import * 

def leaning_arc(vangle, hangle, material, original_sp, numberOfBlocks = random.randint(35, 45)):
    sp = original_sp.copy()
    for _ in range(numberOfBlocks):
        dy = math.sin(math.radians(vangle))
        hyp2 = math.cos(math.radians(vangle)) 
        dx = math.sin(math.radians(hangle)) * hyp2
        dz = math.cos(math.radians(hangle)) * hyp2
        sp['x'] += dx 
        sp['z'] += dz
        sp['y'] += dy
        if vangle >= 90 and vangle <= 265:
            mc.setBlock(sp['x'], sp['y'], sp['z'], material)
            vangle += 100 / numberOfBlocks
        elif vangle <= 90 or vangle >= 275:
            mc.setBlock(sp['x'], sp['y'], sp['z'], material)
            vangle -= 100 / numberOfBlocks
            