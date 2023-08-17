from mcpi import block
import math
import random
import time 
import sys
sys.path.insert(0, '')

from utils.startPoint import *
from utils.leaning_arc import *

def shooting_firework(vangle, hangle, material, original_sp, numberOfBlocks):
    sp = original_sp.copy()
    ep = original_sp.copy()
    endVangle = vangle
    endHangle = hangle

    for blockNumber in range(numberOfBlocks):
        dy = math.sin(math.radians(vangle))
        hyp2 = math.cos(math.radians(vangle)) 
        dx = math.sin(math.radians(hangle)) * hyp2
        dz = math.cos(math.radians(hangle)) * hyp2
        sp['x'] += dx 
        sp['z'] += dz
        sp['y'] += dy
        mc.setBlock(sp['x'], sp['y'], sp['z'], material)
        time.sleep(0.05)
        vangle += 2
        if blockNumber > 4:
            dy = math.sin(math.radians(endVangle))
            hyp2 = math.cos(math.radians(endVangle)) 
            dx = math.sin(math.radians(endHangle)) * hyp2
            dz = math.cos(math.radians(endHangle)) * hyp2
            ep['x'] += dx 
            ep['z'] += dz
            ep['y'] += dy
            mc.setBlock(ep['x'], ep['y'], ep['z'], block.AIR.id)
            endVangle += 2

    for _ in range(100):
        vangle = random.randint(1, 359)
        hangle = random.randint(1, 359)
        material = block.WOOL.id, random.randint(0,15)
        leaning_arc(vangle, hangle, material, sp)

    for n in range(45):
        mc.setBlocks(sp['x'] + n, sp['y'] + n, sp['z'] + n, sp['x'] - n, sp['y'] - n, sp['z'] - n, block.AIR.id)
        time.sleep(0.1)

sp = getStartPoint()
shooting_firework(50, 40, block.GLOWSTONE_BLOCK.id, sp, 75)

