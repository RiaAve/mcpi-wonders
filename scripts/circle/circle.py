from mcpi import minecraft, block
import math
mc = minecraft.Minecraft.create("144.24.195.176")
playerTile = mc.player.getTilePos()
sx = playerTile.x
sz = playerTile.z

for a in range(0,360):
    x = math.cos(math.radians(a)) * 50 + sx
    z = math.sin(math.radians(a)) * 50 + sz
    
    mc.setBlock(x,playerTile.y,z,block.GLASS.id)
