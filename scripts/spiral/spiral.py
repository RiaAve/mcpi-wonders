from mcpi import block
import math
import sys
sys.path.insert(0, '')

from utils.startPoint import mc

playerTile = mc.player.getTilePos()
sx = playerTile.x
sz = playerTile.z

radius = 0

for o in range(5):
    for a in range(0,360):
        radius += 0.01
        x = math.cos(math.radians(a)) * radius + sx
        z = math.sin(math.radians(a)) * radius + sz
        
        mc.setBlock(x,playerTile.y,z,block.GLASS.id)
