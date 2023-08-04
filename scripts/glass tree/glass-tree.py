from mcpi import block
import sys

sys.path.insert(0, '')

from utils.startPoint import *
    
sp = getStartPoint()

for n in range(10):
    length = 10 - n
    x1 = sp['x'] - length
    x2 = sp['x'] + length
    y = sp['y'] + 5 + n * 3
    z1 = sp['z'] - length
    z2 = sp['z'] + length

    mc.setBlocks(x1, y, sp['z'], x2, y, sp['z'], block.GLASS.id)
    mc.setBlocks(sp["x"], y, z1, sp['x'], y, z2, block.GLASS.id)
    
    for s in range(9 - n):
        mc.setBlock(sp['x'] - s, y,sp['z'] - s,block.GLASS.id)
        mc.setBlock(sp['x'] + s, y,sp['z'] + s,block.GLASS.id)
        mc.setBlock(sp['x'] - s, y,sp['z'] + s,block.GLASS.id)
        mc.setBlock(sp['x'] + s, y,sp['z'] - s,block.GLASS.id)
    
mc.setBlocks(sp["x"], sp['y'], sp['z'], sp['x'], sp['y'] + 33, sp['z'], block.WOOD.id, 2)
mc.setBlock(sp['x'], sp['y'] + 34, sp['z'],block.TORCH.id)