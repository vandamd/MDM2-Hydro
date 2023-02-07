from Constants import *

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt




# ----- PUMPING WATER -----
# Function to calculate the total head when pumping 
def pTotalHead(velocity, topDepth, maximumDepth, baseToBase):

    length = baseToBase

    H_s = baseToBase + topDepth - (maximumDepth - topDepth)             # Static Head (Stays the same throughout the entire process)
    H_L = f * (length)/(innerD) * (velocity)/(2 * g)                    # Head Loss (Will increase as the velocity increases)
    H = H_s + H_L                                                       # Total Head from Top to Bottom (will increase as the velocity increases)

    return H

# Function to calculate the volume of water in the top tank
def pTopVolume(flowRates, lastVolume, maximumVolume):
    dt = 1
    volume = lastVolume + flowRates[-1] * dt

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

# Function to calculate the flow rate of top tank dumping water into the bottom tank in cubic meters per second
def topRate(inputPower, H):
    flowrateToTop = (inputPower * pumpEfficiency)/(waterDensity * g * H)

    return flowrateToTop

# Function to calculate the velocity of the water going up the pipe
def velocityUp(flowrateToTop):
    velocityUp = (flowrateToTop / (math.pi * ((0.5 * innerD) ** 2)))

    return velocityUp

# Function to calculate the Heads, Flow Rates and Velocities of the water going up the system
def pumpWater(initialTankDepth, initialVolume, baseToBase, pumpPower):
    totalHeads = []
    topRates = []
    velocities = [0,]
    topDepths = [0,]
    topVolumes = [0, ] 
    bottomVolumes = [initialVolume, ]
    maximumDepth = initialTankDepth
    
    for i in range(len(t)):
        
        totalHeads.append(pTotalHead(velocities[i], topDepths[i], maximumDepth, baseToBase))
        topRates.append(topRate(pumpPower, totalHeads[i]))
        velocities.append(velocityUp(topRates[i]))
        topVolumes.append(pTopVolume(topRates, topVolumes[i-1], initialVolume))
        bottomVolumes.append(pBottomVolume(topRates, bottomVolumes[i-1], initialVolume))

        topDepth = topVolumes[i] * surfaceArea

        if topDepth >= maximumDepth:
            topDepth = maximumDepth
            topRates[-1] = 0
            velocities[-1] = 0
        
        topDepths.append(topDepth)

    return totalHeads, topRates, velocities, topVolumes, bottomVolumes, topDepths






# # ----- DUMPING WATER -----
# # Function to calculate the total head when dumping 
# def dTotalHead(velocity, bottomDepth):
#     H_s = baseToBase - bottomDepth + (initialBottomDepth - bottomDepth)          # Static Head (Stays the same throughout the entire process)
#     H_L = f * (Length)/(innerD) * (velocity)/(2 * g)                              # Head Loss (Will increase as the velocity increases)
#     H = H_s - H_L                                                                 # Total Head from Bottom to Top (will decrease as the velocity increases)

#     return H

# # Function to calculate the volume of water in the bottom tank
# def dBottomVolumes(flowRates, initialVolume, t):
#     volumes = [initialVolume]

#     for i in range(1, len(t)):
#         dt = t[i] - t[i-1]
#         volumes.append(volumes[i-1] + flowRates[i-1] * dt)

#     # If the volume of water in the bottom tank is less than the minimum volume, set it to the minimum volume
#     for i in range(len(volumes)):
#         if volumes[i] < minimumVolume:
#             volumes[i] = minimumVolume
    
#     for i in range(len(volumes)):
#         if volumes[i] > maximumVolume:
#             volumes[i] = maximumVolume

#     return volumes

# # Function to calculate the volume of water in the top tank
# def dTopVolumes(flowRates, initialVolume, t):
#     volumes = [initialVolume]

#     for i in range(1, len(t)):
#         dt = t[i] - t[i-1]
#         volumes.append(volumes[i-1] - flowRates[i-1] * dt)

#     # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
#     for i in range(len(volumes)):
#         if volumes[i] < minimumVolume:
#             volumes[i] = minimumVolume
    
#     for i in range(len(volumes)):
#         if volumes[i] > maximumVolume:
#             volumes[i] = maximumVolume

#     return volumes

# # Function to calculate the flow rate of water going through the turbine in cubic meters per second
# def bottomRate(velocity):
#     # The percentage openess of the turbine
#     Tv = 1

#     flowrateToTurbine = Tv * ((0.5 * innerD) ** 2) * velocity

#     return flowrateToTurbine

# # Function to calculate the velocity of the water going down the pipe
# def velocityDown(bottomRate):
#     velocityDown = (bottomRate / (math.pi * ((0.5 * innerD) ** 2)))

#     return velocityDown

# # Function to calculate the Heads, Flow Rates and Velocities of the water going down the system
# def dumpWater():
#     totalHeads = []
#     bottomRates = []
#     velocities = [0,]
#     bottomDepths = [initialBottomDepth,]
#     initialBottomVolume = maximumVolume 

#     for i in range(len(t)):
#         totalHeads.append(dTotalHead(velocities[i], bottomDepths[i]))
#         bottomRates.append(bottomRate(velocities[i]))
#         velocities.append(velocityDown(bottomRates[i]))

#         bottomVolume = initialBottomVolume - (bottomRates[i] * (t[i] - t[i-1]))
#         if bottomVolume > maximumVolume:
#             bottomVolume = maximumVolume
#         elif bottomVolume < minimumVolume:
#             bottomVolume = minimumVolume

#         bottomDepth = bottomDepths[i] - bottomVolume * surfaceArea
#         if bottomDepth < minimumDepth:
#             bottomDepth = minimumDepth
        
#         bottomDepths.append(bottomDepth)

#     tVolumes = dTopVolumes(bottomRates, maximumVolume, t)
#     bVolumes = dBottomVolumes(bottomRates, minimumVolume, t)

#     return totalHeads, bottomRates, velocities, tVolumes, bVolumes, bottomDepths








