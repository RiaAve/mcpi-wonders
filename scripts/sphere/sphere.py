import math
from mcpi import block
import sys
sys.path.insert(0, '')
from utils.startPoint import * 
sp = getStartPoint()

def sphere(radius):

    for hangle in range(180):
        for vangle in range(360):
            x = math.cos(math.radians(vangle)) 
            y = math.sin(math.radians(vangle)) 
            z = math.sin(math.radians(hangle)) 
            nx = math.cos(math.radians(hangle)) * x
            
            mc.setBlock(nx * radius + sp['x'], y * radius + sp['y'] + 20, z * x * radius + sp['z'],block.GLOWSTONE_BLOCK.id)
        
sphere(25)