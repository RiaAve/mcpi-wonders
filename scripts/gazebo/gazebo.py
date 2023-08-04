from mcpi import block

import sys
sys.path.insert(0, '')

from utils.startPoint import *

sp = getStartPoint()

mc.setBlocks(sp["x"], sp["y"], sp["z"], sp["x"], sp["y"] + 10, sp["z"], block.WOOD_PLANKS.id, 0)

mc.setBlocks(sp["x"] + 20, sp["y"], sp["z"], sp["x"] + 20, sp["y"] + 10, sp["z"], block.WOOD_PLANKS.id, 0)

mc.setBlocks(sp["x"], sp["y"], sp["z"] + 20, sp["x"], sp["y"] + 10, sp["z"] + 20, block.WOOD_PLANKS.id, 0)

mc.setBlocks(sp["x"] + 20, sp["y"], sp["z"] + 20, sp["x"] + 20, sp["y"] + 10, sp["z"] + 20, block.WOOD_PLANKS.id, 0)       
    
topColumnA = {
        "x": sp['x'],
        "y": sp['y'] + 10,
        "z": sp['z']
        }
topColumnB = {
        "x": sp['x'] + 20,
        "y": sp['y'] + 10,
        "z": sp['z']
        }
topColumnC = {
        "x": sp['x'] + 20,
        "y": sp['y'] + 10,
        "z": sp['z'] + 20
        }
topColumnD = {
        "x": sp['x'],
        "y": sp['y'] + 10,
        "z": sp['z'] + 20
        }

while True:
    
    mc.setBlocks(topColumnA['x'],topColumnA['y'],topColumnA['z'],topColumnB['x'],topColumnB['y'],topColumnB['z'], block.WOOD_PLANKS.id, 0)
    mc.setBlocks(topColumnB['x'],topColumnB['y'],topColumnB['z'],topColumnC['x'],topColumnC['y'],topColumnC['z'], block.WOOD_PLANKS.id, 0)
    mc.setBlocks(topColumnC['x'],topColumnC['y'],topColumnC['z'],topColumnD['x'],topColumnD['y'],topColumnD['z'], block.WOOD_PLANKS.id, 0)
    mc.setBlocks(topColumnD['x'],topColumnD['y'],topColumnD['z'],topColumnA['x'],topColumnA['y'],topColumnA['z'], block.WOOD_PLANKS.id, 0)
    
    if topColumnA == topColumnB:
        break
    
    topColumnA['x'] += 1
    topColumnA['y'] += 1
    topColumnA['z'] += 1
    
    topColumnB['x'] -= 1
    topColumnB['y'] += 1
    topColumnB['z'] += 1
    
    topColumnC['x'] -= 1
    topColumnC['y'] += 1
    topColumnC['z'] -= 1
    
    topColumnD['x'] += 1
    topColumnD['y'] += 1
    topColumnD['z'] -= 1
    
    