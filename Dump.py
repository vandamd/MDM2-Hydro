from Constants import *

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pprint as pp

# ----- Dumping Water -----

def dumpWater(initialTankDepth, initialVolume, baseToBase, surfaceArea, innerDiameter, turbineOpeness):
    totalHeads = []
    bottomRates = []
    velocities = [0,]
    topDepths = [initialTankDepth,]
    topVolumes = [initialVolume, ] 
    bottomVolumes = [0, ]
    maximumDepth = initialTankDepth

    for i in range(len(t)):
        totalHeads.append(dTotalHead(velocities[i], topDepths[i], maximumDepth, baseToBase, innerDiameter))
        bottomRates.append(bottomRate(innerDiameter, totalHeads[i], turbineOpeness))
        velocities.append(velocityDown(totalHeads[i-1]))
        topVolumes.append(dTopVolume(bottomRates, topVolumes[i-1], initialVolume))
        bottomVolumes.append(dBottomVolume(bottomRates, bottomVolumes[i-1], initialVolume))

        topDepth = topVolumes[i] * surfaceArea

        if topDepth <= 0:
            topDepth = 0
            bottomRates[-1] = 0
            velocities[-1] = 0

        topDepths.append(topDepth)

    pp.pprint(totalHeads[:20])
    return totalHeads, bottomRates, velocities, topVolumes, bottomVolumes, topDepths

def dTotalHead(velocity, topDepth, maximumDepth, baseToBase, innerDiameter):

    length = baseToBase

    H_s = baseToBase + topDepth - (maximumDepth - topDepth)             # Static Head (Stays the same throughout the entire process)
    H_L = f * (length)/(innerDiameter) * (velocity)/(2 * g)             # Head Loss (Will increase as the velocity increases)
    H = H_s - H_L                                                       # Total Head from Top to Bottom (will increase as the velocity increases)

    return H

def bottomRate(innerDiameter, H, Tv):
    # flowrateToTurbine = Tv * ((math.pi * (0.5 * innerDiameter) ** 2) / 100) * velocity
    flowrateToTurbine = (Tv / 100) * (math.pi * (0.5 * innerDiameter) ** 2) * ((2 * g * H) ** 0.5)

    return flowrateToTurbine

def velocityDown(head):
    velocity = (2 * g * head) ** 0.5

    return velocity

def dTopVolume(flowRates, lastVolume, maximumVolume):
    dt = 1
    volume = lastVolume - flowRates[-1] * dt

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    if volume < 0:
        volume = 0
    
    if volume > maximumVolume:
        volume = maximumVolume

    return volume

def dBottomVolume(flowRates, lastVolume, maximumVolume):
    dt = 1

    volume = lastVolume + flowRates[-1] * dt

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    if volume < 0:
        volume = 0
 
    if volume > maximumVolume:
        volume = maximumVolume

    return volume
