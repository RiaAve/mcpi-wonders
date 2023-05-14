from mcpi import minecraft,block
import time
import random
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
ep = {
    "x": sp["x"] + 20,
    "z": sp["z"] + 20,
    'y': sp['y']
    }

while True:
    mc.setBlocks(sp["x"], sp["y"], sp["z"], ep["x"], ep["y"], ep["z"], block.WATER.id)
    if sp == ep:
        break
    sp = {
        'x': sp["x"] + 1,
        'z': sp["z"] + 1,
        'y': sp["y"] + 1
        }
    ep = {
        'x': ep["x"] - 1,
        'z': ep["z"] - 1,
        'y': ep["y"] + 1
        }

Sp = getStartPoint()
Ep = {
    "x": Sp["x"] + 20,
    "z": Sp["z"] + 20,
    'y': Sp['y']
    }

while True:
    mc.setBlocks(Sp["x"], Sp["y"], Sp["z"], Ep["x"], Ep["y"], Ep["z"], block.GLASS.id)
    if Sp == Ep:
        break
    Sp = {
        'x': Sp["x"] + 1,
        'z': Sp["z"] + 1,
        'y': Sp["y"] - 1
        }
    Ep = {
        'x': Ep["x"] - 1,
        'z': Ep["z"] - 1,
        'y': Ep["y"] - 1
        }