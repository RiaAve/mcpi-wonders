from mcpi import block
import math
import sys
sys.path.insert(0, '')

from utils.startPoint import mc

playerTile = mc.player.getTilePos()
sx = playerTile.x
sz = playerTile.z

height = 0

for o in range(5):
    for a in range(0,360):
        height += 0.08
        x = math.cos(math.radians(a)) * 8 + sx
        z = math.sin(math.radians(a)) * 8 + sz
        
        mc.setBlock(x, playerTile.y + height, z, block.WOOL.id, 14)

        x = math.cos(math.radians(a + 180)) * 8 + sx
        z = math.sin(math.radians(a + 180)) * 8 + sz
        mc.setBlock(x, playerTile.y + height, z, block.WOOL.id, 11)