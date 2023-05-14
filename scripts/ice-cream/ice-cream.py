from mcpi import minecraft, block
import math
import random

mc = minecraft.Minecraft.create("144.24.195.176")
playerTile = mc.player.getTilePos()
sx = playerTile.x
sz = playerTile.z

def drawIceCream():
    for n in range(0,25):
        for a in range(0,360):
            t = 25 - math.pow(1.14, n)
            x = math.cos(math.radians(a)) * t + sx
            z = math.sin(math.radians(a)) * t + sz
            if n == 24:
                mc.setBlock(x,playerTile.y + 50 + n,z,block.WOOL.id, 14)
            else:
                colour = random.choice([0, 0, 0, 0, 0, 12]) 
                mc.setBlock(x,playerTile.y + 50 + n,z,block.WOOL.id, colour)
        
def drawCone():
    for n in range(0,50):
        for a in range(0,360):
            t = 0.5*n 
            x = math.cos(math.radians(a)) * t + sx
            z = math.sin(math.radians(a)) * t + sz
            mc.setBlock(x,playerTile.y + n,z,block.WOOD_PLANKS.id, 2)

def cherry(point):
    for floor in range(0,3):
        mc.setBlocks(
            point['x'] - 3 + floor,
            point['y'],
            point['z'] - 3 + floor,
            point['x'] + 2 - floor,
            point['y'] + floor,
            point['z'] + 2 - floor,
            block.WOOL.id, 14)

cherryStartPoint = {
    'x': playerTile.x,
    'y': playerTile.y + 75,
    'z': playerTile.z
    }

drawCone()
drawIceCream()
cherry(cherryStartPoint)

