from mcpi import minecraft

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