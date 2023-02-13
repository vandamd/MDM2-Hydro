from Constants import *

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pprint as pp

# ----- Dumping Water -----

# Function to calculate the Heads, Flow Rates and Velocities of the water going down the system
def dumpWater(initialVolume, baseToBase, surfaceArea, innerDiameter, turbineOpeness):
    initialTankDepth = initialVolume / surfaceArea 
    totalHeads = []
    bottomRates = []
    velocities = [0,]
    topDepths = [initialTankDepth,]
    topVolumes = [initialVolume, ] 
    bottomVolumes = [0, ]
    maximumDepth = initialTankDepth
    turbinePower = []
    turbineEnergy = [0,]

    for i in range(len(t)):
        totalHeads.append(dTotalHead(velocities[i], topDepths[i], maximumDepth, baseToBase, innerDiameter))
        bottomRates.append(bottomRate(innerDiameter, totalHeads[i], turbineOpeness))
        velocities.append(velocityDown(totalHeads[i-1]))
        topVolumes.append(dTopVolume(bottomRates, topVolumes[i-1], initialVolume))
        bottomVolumes.append(dBottomVolume(bottomRates, bottomVolumes[i-1], initialVolume))
        turbinePower.append(turbineOutputPower(bottomRates, totalHeads))
        turbineEnergy.append(turbineOutputEnergy(turbinePower, turbineEnergy[i-1]))
        topDepths.append(dTopDepth(topVolumes[i], surfaceArea))

        if topDepths[-1] <= 0:
            topDepths[-1] = 0
            bottomRates[-1] = 0
            velocities[-1] = 0
            turbineEnergy[-1] = 0

    # Find the time taken to reach the maximum depth in the bottom tank
    for j in range(len(topDepths)):
        if topDepths[j] == 0:
            timeToMaxDepth = j
            break
    
    totalEnergy = max(turbineEnergy)
    
    return totalHeads, bottomRates, velocities, topVolumes, bottomVolumes, topDepths, timeToMaxDepth, turbineEnergy, totalEnergy

# Function to calculate the total head when dumping
def dTotalHead(velocity, topDepth, maximumDepth, baseToBase, innerDiameter):

    length = baseToBase

    H_s = baseToBase + topDepth - (maximumDepth - topDepth)             # Static Head (Stays the same throughout the entire process)
    H_L = f * (length)/(innerDiameter) * (velocity)/(2 * g)             # Head Loss (Will increase as the velocity increases)
    H = H_s - H_L                                                       # Total Head from Top to Bottom (will increase as the velocity increases)

    return H

# Function to calculate the flow rate of water going down the system
def bottomRate(innerDiameter, H, Tv):
    # flowrateToTurbine = Tv * ((math.pi * (0.5 * innerDiameter) ** 2) / 100) * velocity
    flowrateToTurbine = (Tv / 100) * (math.pi * (0.5 * innerDiameter) ** 2) * ((2 * g * H) ** 0.5)

    return flowrateToTurbine

# Function to calculate the velocity of water going down the system
def velocityDown(head):
    velocity = (2 * g * head) ** 0.5

    return velocity

# Function to calculate the volume of water in the top tank
def dTopVolume(flowRates, lastVolume, maximumVolume):
    dt = 1
    volume = lastVolume - flowRates[-1] * dt

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    if volume < 0:
        volume = 0
    
    if volume > maximumVolume:
        volume = maximumVolume

    return volume

# Function to calculate the volume of water in the bottom tank
def dBottomVolume(flowRates, lastVolume, maximumVolume):
    dt = 1

    volume = lastVolume + flowRates[-1] * dt

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    if volume < 0:
        volume = 0
 
    if volume > maximumVolume:
        volume = maximumVolume

    return volume

# Function to calculate the turbine output power using (bottomRates)*(totalHeads)*(density of water)*(gravity)*(turbine efficiency)
def turbineOutputPower(bottomRates, totalHeads):
    power = bottomRates[-1] * totalHeads[-1] * waterDensity * g * turbineEfficiency

    return power

# Function to calculate the turbine output energy using turbine output power and time
def turbineOutputEnergy(power, lastEnergy):
    dt = 1

    energy = lastEnergy + power[-1] * dt

    return energy

# Function to calculate the depth of water in the top tank
def dTopDepth(topVolumes, surfaceArea):

    topDepth = (topVolumes * surfaceArea)

    return topDepth