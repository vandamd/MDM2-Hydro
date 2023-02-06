from Constants import *

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ----- SHARED -----
# Function to calculate the total head 
def totalHead(velocity):
    H_s = baseToBase + topDepth - bottomDepth                           # Static Head (Stays the same throughout the entire process)
    H_L = f * (Length)/(innerD) * (velocity)/(2 * g)                    # Head Loss (Will increase as the velocity increases)
    H = H_s + H_L                                                       # Total Head from Top to Bottom (will increase as the velocity increases)

    return H


# ----- PUMPING WATER -----
# Function to calculate the volume of water in the top tank
def pTopVolumes(flowRates, initialVolume, t):
    volumes = [initialVolume]

    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        volumes.append(volumes[i-1] + flowRates[i-1] * dt)

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    for i in range(len(volumes)):
        if volumes[i] < minimumVolume:
            volumes[i] = minimumVolume
    
    for i in range(len(volumes)):
        if volumes[i] > maximumVolume:
            volumes[i] = maximumVolume

    return volumes

# Function to calculate the volume of water in the bottom tank
def pBottomVolumes(flowRates, initialVolume, t):
    volumes = [initialVolume]

    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        volumes.append(volumes[i-1] - flowRates[i-1] * dt)

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    for i in range(len(volumes)):
        if volumes[i] < minimumVolume:
            volumes[i] = minimumVolume
    
    for i in range(len(volumes)):
        if volumes[i] > maximumVolume:
            volumes[i] = maximumVolume

    return volumes

# Function to calculate the flow rate of top tank dumping water into the bottom tank
def topRate(inputPower, H):
    flowrateToTop = (inputPower * pumpEfficiency)/(waterDensity * g * H)

    return flowrateToTop

# Function to calculate the velocity of the water going up the pipe
def velocityUp(flowrateToTop):
    velocityUp = (flowrateToTop / (math.pi * ((0.5 * innerD) ** 2)))

    return velocityUp

# Function to calculate the Heads, Flow Rates and Velocities of the water going up the system
def pumpWater():
    totalHeads = []
    topRates = []
    velocities = [0,]
    outputPowers = []
    
    for i in range(len(t)):
        totalHeads.append(totalHead(velocities[i]))
        topRates.append(topRate(inputPower, totalHeads[i]))
        velocities.append(velocityUp(topRates[i]))

    tVolumes = pTopVolumes(topRates, minimumVolume, t)
    bVolumes = pBottomVolumes(topRates, maximumVolume, t)

    return totalHeads, topRates, velocities, tVolumes, bVolumes

# TODO: Function to calculate the power output of the pump




# ----- DUMPING WATER -----
def dTopVolumes(flowRates, initialVolume, t):
    volumes = [initialVolume]

    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        volumes.append(volumes[i-1] - flowRates[i-1] * dt)

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    for i in range(len(volumes)):
        if volumes[i] < minimumVolume:
            volumes[i] = minimumVolume
    
    for i in range(len(volumes)):
        if volumes[i] > maximumVolume:
            volumes[i] = maximumVolume

    return volumes

def dBottomVolumes(flowRates, initialVolume, t):
    volumes = [initialVolume]

    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        volumes.append(volumes[i-1] + flowRates[i-1] * dt)

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    for i in range(len(volumes)):
        if volumes[i] < minimumVolume:
            volumes[i] = minimumVolume
    
    for i in range(len(volumes)):
        if volumes[i] > maximumVolume:
            volumes[i] = maximumVolume

    return volumes

# def bottomRate(inputPower, H):

# Previously, we assumed that the flow rate going down the system (dumping) was constant,
# but now we know that it's not constant and that it changes due to the change in volume of the top tank (weight of water descreasing)
# and other factures such as the change in Head (H). 

# def velocityDown(flowrateToBottom):

# def dumpWater():












# # Function for the change in volume of the top tank
# def topRate(topVolume, t, flowrateToBottom, inputPower, H_TB):
#     flowrateToTop = (inputPower * pumpEfficiency)/(waterDensity * g * H_TB)

#     dV_topdt = flowrateToTop + precip - evap - flowrateToBottom

#     return dV_topdt

# # Function for the change in volume of the bottom tank
# def bottomRate(bottomVolume, t, flowrateToBottom, inputPower, H_TB):
#     flowrateToTop = (inputPower * pumpEfficiency)/(waterDensity * g * H_TB)

#     dV_bottomdt = flowrateToBottom + precip - evap - flowrateToTop

#     return dV_bottomdt

# # Function to calculate the velocity of the water going down the pipe
# def velocityDown(flowrateToBottom):
#     velocitiesDown = []
#     for i in range(len(t)):
#         velocitiesDown.append(flowrateToBottom / (math.pi * ((0.5 * innerD) ** 2)))

#     return velocitiesDown

# # Function to calculate the velocity of the water going up the pipe
# def velocityUp(flowrateToTop, t):
#     velocitiesUp = []
#     for i in range(len(t)):
#         velocitiesUp.append(flowrateToTop / (math.pi * ((0.5 * innerD) ** 2)))

#     return velocitiesUp




# # Function to dump the water from the top tank to the bottom tank
# def dumpWater(initialTopVolume, initialBottomVolume, inputPower):
#     # Volume of water in the top tank
#     topVolume = odeint(topRate, initialTopVolume, t, args=(flowrateToBottom, inputPower, H_TB))
#     # Volume of water in the bottom tank
#     bottomVolume = odeint(bottomRate, initialBottomVolume, t, args=(flowrateToBottom, inputPower, H_TB))

#     return topVolume, bottomVolume