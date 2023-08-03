from mcpi import minecraft,block
import time
import random
import math
mc = minecraft.Minecraft.create("144.24.195.176")

def getStartPoint():
    direction = mc.player.getDirection()

    playerTile = mc.player.getTilePos()

    dx = direction.x * 5 * (abs(direction.y) + 1)
    dz = direction.z * 5 * (abs(direction.y) + 1)

    startpointx = playerTile.x + dx 
    startpointz = playerTile.z + dz

    return {
        "x": startpointx,
        "z": startpointz,
        "y": playerTile.y
        }

sp = getStartPoint()

for layer in range(20):
    for side in range(3):
        angle = side * 120 + 15
        for blockNumber in range(20 - layer):
            if blockNumber > layer:
                dx = math.cos(math.radians(angle)) 
                dz = math.sin(math.radians(angle)) 
                sp['x'] += dx
                sp['z'] += dz
                mc.setBlock(sp['x'], sp["y"], sp['z'], block.GRASS.id)
    sp['y'] += 1
    startdx = math.cos(math.radians(45)) 
    startdz = math.sin(math.radians(45)) 
    sp['x'] += startdx
    sp['z'] += startdz    
    
