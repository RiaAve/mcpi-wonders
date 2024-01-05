import math
from mcpi import block
import sys
sys.path.insert(0, '')
from utils.startPoint import * 
sp = getStartPoint() 

def sphere(radius, startY, blockColourFn, buildExtraFn = None):
    for hangle in range(180):
        for vangle in range(360):
            blockId = blockColourFn(vangle, hangle)
            x = math.cos(math.radians(vangle)) 
            y = math.sin(math.radians(vangle)) 
            z = math.sin(math.radians(hangle)) 
            nx = math.cos(math.radians(hangle)) * x

            bx = nx * radius + sp['x'] 
            by = y * radius + startY
            bz = z * x * radius + sp['z']

            if buildExtraFn != None :
                buildExtraFn(vangle, hangle, bx, by, bz)

            mc.setBlock(bx, by, bz, blockId) 

def bodyBlockColour(vangle, hangle):
    middleButtonCond = 179 <= vangle <= 181 and 88 <= hangle <= 92
    topButtonCond = 159 <= vangle <= 163 and 88 <= hangle <= 92
    bottomButtonCond = 199 <= vangle <= 203 and 88 <= hangle <= 92

    colour = 15 if middleButtonCond or topButtonCond or bottomButtonCond else 0
    return block.WOOL.id, colour

def headBlockColour(vangle, hangle):
    leftEyeCondition = 147 <= vangle <= 153 and 72 <= hangle <= 78
    rightEyeCondition = 147 <= vangle <= 153 and 100 <= hangle <= 110
    smileCond = 197 <= vangle <= 203 and 73 <= hangle <= 107
    if leftEyeCondition or rightEyeCondition or smileCond :
        colour = 15 
    else :
        colour = 0 
    return block.WOOL.id, colour

def nose(vangle, hangle, bx, by, bz):
    if 178 <= vangle <= 182 and 88 <= hangle <= 92:
        mc.setBlocks(bx, by, bz, bx, by, bz - 6, block.WOOL.id, 1)
    
sphere(15, sp['y'] + 20, bodyBlockColour)
sphere(10, sp['y'] + 43, headBlockColour, nose)
