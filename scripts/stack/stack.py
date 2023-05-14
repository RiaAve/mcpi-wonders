from mcpi import minecraft, block
import math
import random
mc = minecraft.Minecraft.create("144.24.195.176")

def getStartPoint(distance):
    direction = mc.player.getDirection()

    playerTile = mc.player.getTilePos()

    yProjection = math.sqrt(1 - direction.y ** 2)
    
    zProjection = direction.z / yProjection
    xProjection = direction.x / yProjection
    
    x = playerTile.x + xProjection * distance
    z = playerTile.z + zProjection * distance
    
    return {
        "x": x,
        "z": z,
        "y": playerTile.y
        }
    
sp = getStartPoint(5)

for n in range(0,100):
    dx = random.randint(-1, 1)
    dz = random.randint(-1, 1)
    sp['x'] = sp['x'] + dx
    sp['z'] = sp['z'] + dz
    woolType= random.randint(0,15)
    mc.setBlocks(sp['x'], sp['y'] + n, sp['z'],sp['x'] + 4, sp['y'] + n, sp['z'] + 4,block.WOOL.id, woolType)