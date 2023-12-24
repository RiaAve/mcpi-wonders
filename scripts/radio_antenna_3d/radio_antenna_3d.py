import math
from mcpi import block
import sys
sys.path.insert(0, '')
from utils.startPoint import * 
sp = getStartPoint() 

sp['x'] += 20

def pyramid(height, angle):
    nx = sp['x'] 
    nz = sp['z']
    ny = sp['y']
    baseWidth = height / math.tan(math.radians(angle)) * 2
    ex = nx + baseWidth
    ez = nz + baseWidth

    for _ in range(height):
        mc.setBlocks(nx, ny, nz, ex, ny, ez, block.STONE.id)
        ny += 1
        nx += 1 / math.tan(math.radians(angle))
        nz += 1 / math.tan(math.radians(angle))
        ex -= 1 / math.tan(math.radians(angle))
        ez -= 1 / math.tan(math.radians(angle))

    return baseWidth

def sphere(radius):

    hangle = 25

    for _ in range(5): 
        for hangle in range(360):
            if hangle % 60 == 0:
                for vangle in range(360):
                    if vangle <= 45 or (vangle >= 135 and vangle <= 225) or vangle >= 315:
                        x = math.cos(math.radians(vangle)) 
                        y = math.sin(math.radians(vangle)) 
                        z = math.sin(math.radians(hangle)) 
                        nx = math.cos(math.radians(hangle)) * x
                            
                        mc.setBlock(nx * radius + centerOfTheSphere['x'], y * radius + centerOfTheSphere['y'], z * x * radius + centerOfTheSphere['z'],block.WOOL.id)
        radius += 5
        
pyramidWidth = pyramid(60, 80)

centerOfTheSphere = {
    'x': sp['x'] + pyramidWidth / 2,
    'y': sp['y'] + 60,
    'z': sp['z'] + pyramidWidth / 2
}

sphere(25)