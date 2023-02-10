from Constants import *

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ----- PUMPING WATER -----

# Function to calculate the Heads, Flow Rates and Velocities of the water going up the system
def pumpWater(initialVolume, baseToBase, pumpPower, surfaceArea, innerDiameter):
    initialTankDepth = initialVolume / surfaceArea 
    totalHeads = []
    topRates = []
    velocities = [0,]
    topDepths = [0,]
    topVolumes = [0, ] 
    bottomVolumes = [initialVolume, ]
    maximumDepth = initialTankDepth
    pumpEnergy = [0,]
    
    for i in range(len(t)):
        totalHeads.append(pTotalHead(velocities[i], topDepths[i], maximumDepth, baseToBase, innerDiameter))
        topRates.append(topRate(pumpPower, totalHeads[i]))
        velocities.append(velocityUp(topRates[i], innerDiameter))
        topVolumes.append(pTopVolume(topRates, topVolumes[i-1], initialVolume))
        bottomVolumes.append(pBottomVolume(topRates, bottomVolumes[i-1], initialVolume))
        pumpEnergy.append(pumpOutputEnergy(pumpPower, pumpEnergy[i-1], topVolumes, initialVolume))

        topDepth = topVolumes[i] / surfaceArea

        if topVolumes[i] == initialVolume:
            # topDepth = initialTankDepth
            topRates[-1] = 0
            velocities[-1] = 0
        
        topDepths.append(topDepth)

    # Find the time taken to reach the maximum depth in the top tank
    for j in range(len(topVolumes)):
        if topVolumes[j] == initialVolume:
            timeToMaxDepth = j
            break
    
    totalEnergy = pumpEnergy[timeToMaxDepth-1]

    return totalHeads, topRates, velocities, topVolumes, bottomVolumes, topDepths, timeToMaxDepth, pumpEnergy, totalEnergy

# Function to calculate the total head when pumping 
def pTotalHead(velocity, topDepth, maximumDepth, baseToBase, innerDiameter):

    H_s = baseToBase + topDepth - (maximumDepth - topDepth)             # Static Head (Stays the same throughout the entire process)
    H_L = f * (baseToBase)/(innerDiameter) * (velocity)/(2 * g)         # Head Loss (Will increase as the velocity increases)
    H = H_s + H_L                                                       # Total Head from Top to Bottom (will increase as the velocity increases)

    return H

# Function to calculate the flow rate of top tank dumping water into the bottom tank in cubic meters per second
def topRate(inputPower, H):
    flowrateToTop = (inputPower * pumpEfficiency)/(waterDensity * g * H)

    return flowrateToTop

# Function to calculate the velocity of the water going up the pipe
def velocityUp(flowrateToTop, innerDiameter):
    velocityUp = (flowrateToTop / (math.pi * ((0.5 * innerDiameter) ** 2)))

    return velocityUp

# Function to calculate the volume of water in the top tank
def pTopVolume(flowRates, lastVolume, maximumVolume):
    dt = 1
    volume = lastVolume + (flowRates[-1] * dt)

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    if volume < 0:
        volume = 0
    
    if volume > maximumVolume:
        volume = maximumVolume

    return volume

# Function to calculate the volume of water in the bottom tank
def pBottomVolume(flowRates, lastVolume, maximumVolume):
    dt = 1

    volume = lastVolume - flowRates[-1] * dt

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    if volume < 0:
        volume = 0
 
    if volume > maximumVolume:
        volume = maximumVolume

    return volume

# Function to calculate the energy used to pump water
def pumpOutputEnergy(pumpPower, lastEnergy, topVolumes, maximumVolume):
    dt = 1

    energy = lastEnergy + (pumpPower * dt)

    if topVolumes[-1] == maximumVolume:
        energy = 0

    return energy


# Function to calculate the depth of water in the top tank
def pTopDepth(topVolumes, surfaceArea):

    topDepth = (topVolumes * surfaceArea)

    return topDepth