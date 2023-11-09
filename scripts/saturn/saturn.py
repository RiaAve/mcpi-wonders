import math
from mcpi import block
import sys
sys.path.insert(0, '')
from utils.startPoint import * 

sp = getStartPoint()

def sphere(radius):

    for hangle in range(360):
        for vangle in range(360):
            x = math.cos(math.radians(vangle)) 
            y = math.sin(math.radians(vangle)) 
            z = math.sin(math.radians(hangle)) 
            nx = math.cos(math.radians(hangle)) * x
            
            mc.setBlock(nx * radius + sp['x'], y * radius + sp['y'] + 30, z * x * radius + sp['z'],block.WOOL.id, 4)
        
sphere(25)
 
def ring(ringWidth, distance, material, type):

    for b in range(ringWidth):
        for a in range(0,360):
                x = math.cos(math.radians(a)) * (distance + b) + sp['x']
                z = math.sin(math.radians(a)) * (distance + b) + sp['z']
                
                mc.setBlock(x,sp['y'] + 30,z,material, type)
            
ring(2, 40, block.WOOL.id, 12)
ring(4, 50, block.WOOL.id, 8)
ring(6, 60, block.GLASS.id, 0)