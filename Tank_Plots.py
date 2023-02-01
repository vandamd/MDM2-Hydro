from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import math

# Hydro Pump
# TODO: Work out how to change the input power and flowrateToBottom based on time
# TODO: Evaporation equation
# TODO: Precipitation equation
# TODO: Head?

# --- Inputs ---
maximumVolume = 1.0             # In cubic meters
minimumVolume = 0.0             # In cubic meters
initialTopVolume = 0            # In cubic meters
initialBottomVolume = 1         # In cubic meters
timeSpan = 86400                # In seconds

t = np.linspace(0,timeSpan,timeSpan)  # Time span in seconds (24 hours)
g = 9.81                        # Gravity in meters per second squared
inputPower = 5                  # Input power in watts
pumpEfficency = 0.8             # Pump efficency
waterDensity = 997              # Density of water in kilograms per cubic meter
pumpHead = 10                   # Pump head in meters

evap = 0.000001                 # Evaporation rate in cubic meters per second
precip = 0.00001                # Precipitation rate in cubic meters per second

# --- Equations ---
# Flow rate from the pump in cubic meters per second (bottom to top tank)
# flowrateToTop = (inputPower * pumpEfficency)/(waterDensity * g * pumpHead)

# It is a choice we make 
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
    inputPower = 5
    flowrateToBottom = 0

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
    inputPower = 5
    flowrateToBottom = 0

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








# Calculate the volume of water in the top and bottom tanks
topVolumes = topVolume(initialTopVolume, t)
bottomVolumes = bottomVolume(initialBottomVolume, t)

# bottomVolume = odeint(bottom, bottomVolume, t)
plt.plot(t, topVolumes, 'b', label='Top Tank')
plt.plot(t, bottomVolumes, label='Bottom Tank', color='red')

# plt.plot(t, bottomVolume, 'b', label='Bottom')
plt.xlabel('time (s)')
plt.ylabel('volume (m^3)')
plt.ylim(-0.1, maximumVolume+0.1)
plt.autoscale(axis='x', tight=True)
plt.legend(loc='best')
plt.grid()
plt.show()
