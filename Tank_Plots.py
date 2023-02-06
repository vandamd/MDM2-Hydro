from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import math

# Hydro Pump
# TODO: Evaporation equation, we're probably just going to give it a constant value
# TODO: Precipitation equation, same idea as evaporation
# TODO: Losses
    # TODO: Friction losses
    # TODO: Dynamic head
# TODO: Functions to pump and dump at separate times
# TODO: Flow rate to bottom tank


# What would the price difference be to make it worth it?

# --- Inputs ---
maximumVolume = 1.0             # In cubic meters
minimumVolume = 0.0             # In cubic meters
timeSpan = 86400                # In seconds
t = np.linspace(0,timeSpan,timeSpan)  # Time span in seconds (24 hours)
g = 9.81                        # Gravity in meters per second squared
pumpEfficency = 0.8             # Pump efficency
waterDensity = 997              # Density of water in kilograms per cubic meter

pumpHead = 10                   # Pump head in meters (ITS THE HEIGHT DIFFERENCE BETWEEN THE TOP OF THE TANK AND PUMP?) Does this mean that we have two differrent heads?

evap = 0.00000                 # Evaporation rate in cubic meters per second
precip = 0.0000                # Precipitation rate in cubic meters per second
initialTopVolume = 1            # In cubic meters
initialBottomVolume = 0        # In cubic meters
inputPower = 5                  # Input power in watts





# --- Equations ---
# Flow rate from the pump in cubic meters per second (bottom to top tank)
# flowrateToTop = (inputPower * pumpEfficency)/(waterDensity * g * pumpHead)

# Flow rate to the bottom in cubic meters per second (top to bottom tank) 
# flowrateToBottom = 0

# Function for the change in volume of the top tank
def toprate(topVolume, t, flowrateToBottom, inputPower):
    flowrateToTop = (inputPower * pumpEfficency)/(waterDensity * g * pumpHead)

    dV_topdt = flowrateToTop + precip - evap - flowrateToBottom

    return dV_topdt

# Function for the change in volume of the bottom tank
def bottomrate(bottomVolume, t, flowrateToBottom, inputPower):
    flowrateToTop = (inputPower * pumpEfficency)/(waterDensity * g * pumpHead)

    dV_bottomdt = flowrateToBottom + precip - evap - flowrateToTop

    return dV_bottomdt

# This returns the volume of water in the top tank
def topVolume(initialTopVolume, t):            
    inputPower = 0
    flowrateToBottom = 0.0001

    # Volume of water in the top tank
    topVolume = odeint(toprate, initialTopVolume, t, args=(flowrateToBottom, inputPower))

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    for i in range(len(topVolume)):
        if topVolume[i] < minimumVolume:
            topVolume[i] = minimumVolume
    
    for i in range(len(topVolume)):
        if topVolume[i] > maximumVolume:
            topVolume[i] = maximumVolume

    return topVolume

# Returns the volume of water in the bottom tank
def bottomVolume(initialBottomVolume, t):
    inputPower = 0
    flowrateToBottom = 0.0001

    # Volume of water in the bottom tank
    bottomVolume = odeint(bottomrate, initialBottomVolume, t, args=(flowrateToBottom, inputPower))

    # If the volume of water in the top tank is less than the minimum volume, set it to the minimum volume
    for i in range(len(bottomVolume)):
        if bottomVolume[i] < minimumVolume:
            bottomVolume[i] = minimumVolume
    
    for i in range(len(bottomVolume)):
        if bottomVolume[i] > maximumVolume:
            bottomVolume[i] = maximumVolume

    return bottomVolume

# Function for the velocity of the water flowing down using topVolume()
def velocityDown(flowrateToBottom):
    velocities = []
    for i in range(len(t)):
        velocities.append(flowrateToBottom / (math.pi * (0.5 ** 2)))

    return velocities


# Calculate the volume of water in the top and bottom tanks
topVolumes = topVolume(initialTopVolume, t)
bottomVolumes = bottomVolume(initialBottomVolume, t)
velocities = velocityDown(0.0001)

# Define figure 
fig = plt.figure()

# Define figure with 2 subplots
subfigs = fig.subfigures(1, 2, wspace=0.7)

axsLeft = subfigs[0].subplots(1, 1)
axsLeft.plot(t, topVolumes, 'b', label='Top Tank')
axsLeft.plot(t, bottomVolumes, label='Bottom Tank', color='red')
axsLeft.set_title('Volume of Water in Tanks')
axsLeft.set_xlabel('Time (s)')
axsLeft.set_ylabel('Volume (m^3)')
axsLeft.legend(loc='best')
axsLeft.grid()

axsRight = subfigs[1].subplots(1, 1)
axsRight.plot(t, velocities, 'g', label='Velocity')
axsRight.set_title('Velocity of Water Flowing Down')
axsRight.set_xlabel('Time (s)')
axsRight.set_ylabel('Velocity (m/s)')
axsRight.legend(loc='best')
axsRight.grid()








# plt.ylim(-0.1, maximumVolume+0.1)
# plt.autoscale(axis='x', tight=True)


plt.show()
