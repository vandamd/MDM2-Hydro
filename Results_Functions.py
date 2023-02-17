from Pump import *
from Dump import *

import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Function to plot the results of the dump
def plotDump(volume, distance, surfaceArea, innerDiameter, turbineOpeness):
    pumpResults = dumpWater(volume, distance, surfaceArea, innerDiameter, turbineOpeness)

    pumpHeads = pumpResults[0]
    pumpRates = pumpResults[1]
    pumpVelocities = pumpResults[2]
    pumpVelocities = pumpVelocities[:-1]
    topTankVolumes = pumpResults[3]
    topTankVolumes = topTankVolumes[:-1]
    bottomTankVolumes = pumpResults[4]
    bottomTankVolumes = bottomTankVolumes[:-1]
    topDepths = pumpResults[5]
    topDepths = topDepths[:-1]
    timeTaken = pumpResults[6]
    energy = pumpResults[7]
    energy = energy[:-1]
    energyTotal = pumpResults[8]

    t = np.linspace(0,timeTaken,timeTaken)

    print("\nTime Taken:", timeTaken, "seconds /", round(timeTaken/60, 2), "minutes /", round(timeTaken/3600, 2), "hours")
    print("Energy Generated:", energyTotal, "Joules /", round(energyTotal/1000, 2), "Kilojoules /", round(energyTotal/1000000, 2), "Megajoules")

    # limit = timeTaken

    # Define figure 
    fig = plt.figure()

    # Define figure with 5 subplots
    subfigs = fig.subfigures(1, 6, wspace=2)

    axsLeft = subfigs[0].subplots(1, 1)
    axsLeft.plot(t, topTankVolumes, 'b', label='Top Tank')
    axsLeft.plot(t, bottomTankVolumes, 'r', label='Bottom Tank')
    axsLeft.legend(loc='best')
    axsLeft.set_title('Volume of Water in the Top Tank')
    axsLeft.set_xlabel('Time (s)')
    axsLeft.set_ylabel('Volume (m^3)')
    axsLeft.grid()
    # axsLeft.set_xlim(-5, limit)

    axsMid1 = subfigs[1].subplots(1, 1)
    axsMid1.plot(t, pumpRates)
    axsMid1.set_title('Flowrate of Water')
    axsMid1.set_xlabel('Time (s)')
    axsMid1.set_ylabel('Flowrate (m^3/s)')
    axsMid1.grid()
    # axsMid1.set_xlim(-5, limit)

    axsMid2 = subfigs[2].subplots(1, 1)
    axsMid2.plot(t, pumpHeads)
    axsMid2.set_title('Head of Water')
    axsMid2.set_xlabel('Time (s)')
    axsMid2.set_ylabel('Head (m)')
    axsMid2.grid()
    # axsMid2.set_xlim(-5, limit)

    axsMid3 = subfigs[3].subplots(1, 1)
    axsMid3.plot(t, topDepths)
    axsMid3.set_title('Depth of Water in the Top Tank')
    axsMid3.set_xlabel('Time (s)')
    axsMid3.set_ylabel('Depth (m)')
    axsMid3.grid()
    # axsMid3.set_xlim(-5, limit)

    axsMid4 = subfigs[4].subplots(1, 1)
    axsMid4.plot(t, energy)
    axsMid4.set_title('Energy generated/used')
    axsMid4.set_xlabel('Time (s)')
    axsMid4.set_ylabel('Energy (J)')
    axsMid4.grid()
    # axsMid4.set_xlim(-5, limit)

    axsRight = subfigs[5].subplots(1, 1)
    axsRight.plot(t, pumpVelocities)
    axsRight.set_title('Velocity of Water')
    axsRight.set_xlabel('Time (s)')
    axsRight.set_ylabel('Velocity (m/s)')
    axsRight.grid()
    # axsRight.set_xlim(-5, limit)

    plt.show()


# Function to plot the results of the pump
def plotPump(volume, distance, pumpPower, surfaceArea, innerDiameter):
    pumpResults = pumpWater(volume, distance, pumpPower, surfaceArea, innerDiameter)

    pumpHeads = pumpResults[0]
    pumpRates = pumpResults[1]
    pumpVelocities = pumpResults[2]
    pumpVelocities = pumpVelocities[:-1]
    topTankVolumes = pumpResults[3]
    topTankVolumes = topTankVolumes[:-1]
    bottomTankVolumes = pumpResults[4]
    bottomTankVolumes = bottomTankVolumes[:-1]
    topDepths = pumpResults[5]
    topDepths = topDepths[:-1]
    timeTaken = pumpResults[6]
    energy = pumpResults[7]
    energy = energy[:-1]
    energyTotal = pumpResults[8]

    t = np.linspace(0,timeTaken,timeTaken)

    print("\nTime Taken:", timeTaken, "seconds /", round(timeTaken/60, 2), "minutes /", round(timeTaken/3600, 2), "hours")
    print("Energy Used:", energyTotal, "Joules /", round(energyTotal/1000, 2), "Kilojoules /", round(energyTotal/1000000, 2), "Megajoules")

    # limit = timeTaken

    # Define figure 
    fig = plt.figure()

    # Define figure with 5 subplots
    subfigs = fig.subfigures(1, 6, wspace=2)

    axsLeft = subfigs[0].subplots(1, 1)
    axsLeft.plot(t, topTankVolumes, 'b', label='Top Tank')
    axsLeft.plot(t, bottomTankVolumes, 'r', label='Bottom Tank')
    axsLeft.legend(loc='best')
    axsLeft.set_title('Volume of Water in the Top Tank')
    axsLeft.set_xlabel('Time (s)')
    axsLeft.set_ylabel('Volume (m^3)')
    axsLeft.grid()
    # axsLeft.set_xlim(-5, limit)

    axsMid1 = subfigs[1].subplots(1, 1)
    axsMid1.plot(t, pumpRates)
    axsMid1.set_title('Flowrate of Water')
    axsMid1.set_xlabel('Time (s)')
    axsMid1.set_ylabel('Flowrate (m^3/s)')
    axsMid1.grid()
    # axsMid1.set_xlim(-5, limit)

    axsMid2 = subfigs[2].subplots(1, 1)
    axsMid2.plot(t, pumpHeads)
    axsMid2.set_title('Head of Water')
    axsMid2.set_xlabel('Time (s)')
    axsMid2.set_ylabel('Head (m)')
    axsMid2.grid()
    # axsMid2.set_xlim(-5, limit)

    axsMid3 = subfigs[3].subplots(1, 1)
    axsMid3.plot(t, topDepths)
    axsMid3.set_title('Depth of Water in the Top Tank')
    axsMid3.set_xlabel('Time (s)')
    axsMid3.set_ylabel('Depth (m)')
    axsMid3.grid()
    # axsMid3.set_xlim(-5, limit)

    axsMid4 = subfigs[4].subplots(1, 1)
    axsMid4.plot(t, energy)
    axsMid4.set_title('Energy generated/used')
    axsMid4.set_xlabel('Time (s)')
    axsMid4.set_ylabel('Energy (J)')
    axsMid4.grid()
    # axsMid4.set_xlim(-5, limit)

    axsRight = subfigs[5].subplots(1, 1)
    axsRight.plot(t, pumpVelocities)
    axsRight.set_title('Velocity of Water')
    axsRight.set_xlabel('Time (s)')
    axsRight.set_ylabel('Velocity (m/s)')
    axsRight.grid()
    # axsRight.set_xlim(-5, limit)

    plt.show()


# Function to dump water then pump water at specific times in the day
def cycleWater(dumpTime, pumpTime, volume, distance, pumpPower, surfaceArea, innerDiameter, turbineOpeness):
    # Convert time to seconds
    dumpTime = int(dumpTime[0:2]) * 3600 + int(dumpTime[3:5]) * 60
    pumpTime = int(pumpTime[0:2]) * 3600 + int(pumpTime[3:5]) * 60

    # Pump water
    pumpResults = pumpWater(volume, distance, pumpPower, surfaceArea, innerDiameter)

    # Dump water
    dumpResults = dumpWater(volume, distance, surfaceArea, innerDiameter, turbineOpeness)

    # Energy Total
    dEnergy = dumpResults[8]
    pEnergy = pumpResults[8]

    # Fill before dumping
    topVolumes = np.full(dumpTime, volume)
    bottomVolumes = np.full(dumpTime, 0)
    netEnergy = np.full(dumpTime, 0)

    # Add dump results
    topVolumes = np.concatenate((topVolumes, dumpResults[3]))
    bottomVolumes = np.concatenate((bottomVolumes, dumpResults[4]))
    netEnergy = np.concatenate((netEnergy, dumpResults[7]))

    # Fill before pumping
    topVolumes = np.concatenate((topVolumes, np.full(pumpTime - dumpTime, 0)))
    bottomVolumes = np.concatenate((bottomVolumes, np.full(pumpTime - dumpTime, volume)))
    netEnergy = np.concatenate((netEnergy, np.full(pumpTime - dumpTime, max(dumpResults[7]))))

    # Add pump results
    topVolumes = np.concatenate((topVolumes, pumpResults[3]))
    bottomVolumes = np.concatenate((bottomVolumes, pumpResults[4]))
    lossEnergy = np.full(len(pumpResults[7]), max(dumpResults[7]))
    lossEnergy = lossEnergy - pumpResults[7]
    netEnergy = np.concatenate((netEnergy, lossEnergy))

    # Fill to end of day
    topVolumes = np.concatenate((topVolumes, np.full(86400 - pumpTime, volume)))
    bottomVolumes = np.concatenate((bottomVolumes, np.full(86400 - pumpTime, 0)))
    netEnergy = np.concatenate((netEnergy, np.full(86400 - pumpTime, netEnergy[-1])))

    t = np.linspace(0, len(topVolumes), len(topVolumes))

    print("\nEnergy Used: ", round(pEnergy, 2), "Joules /", round(pEnergy/1000, 2), "Kilojoules /", round(pEnergy/1000000, 2), "Megajoules")
    print("Energy generated: ", round(dEnergy, 2), "Joules /", round(dEnergy/1000, 2), "Kilojoules /", round(dEnergy/1000000, 2), "Megajoules")
    print("Net Energy: ", round(dEnergy - pEnergy, 2), "Joules /", round((dEnergy - pEnergy)/1000, 2), "Kilojoules /", round((dEnergy - pEnergy)/1000000, 4), "Megajoules")

    # Plot
    fig = plt.figure()

    # Define figure with 5 subplots
    subfigs = fig.subfigures(2, 1)    
    
    axsTop = subfigs[0].subplots(1, 1)
    axsMid = subfigs[1].subplots(1, 1)
    # axsBottom = subfigs[2].subplots(1, 1)

    axsTop.plot(t, topVolumes, 'b', label='Top Tank')
    axsTop.plot(t, bottomVolumes, 'r', label='Bottom Tank')
    axsTop.legend(loc='best')
    axsTop.set_title('Volume of Water in the Tanks')
    axsTop.set_xlabel('Time (s)')
    axsTop.set_ylabel('Volume (m^3)')
    axsTop.grid()

    axsMid.plot(t, netEnergy, 'g', label='Net Energy')
    axsMid.legend(loc='best')
    axsMid.set_title('Net Energy')
    axsMid.set_xlabel('Time (s)')
    axsMid.set_ylabel('Energy (J)')
    axsMid.grid()

    fig.subplots_adjust(bottom=0.15)
    plt.show()

    return netEnergy


# Function to calculate net energy
def netEnergy(volume, distance, pumpPower, surfaceArea, innerDiameter, turbineOpeness):

    # Pump water
    pumpResults = pumpWater(volume, distance, pumpPower, surfaceArea, innerDiameter)

    # Dump water
    dumpResults = dumpWater(volume, distance, surfaceArea, innerDiameter, turbineOpeness)

    # Energy Total
    dEnergy = dumpResults[8]
    pEnergy = pumpResults[8]

    # Net Energy
    netEnergy = dEnergy - pEnergy

    return netEnergy


# Function to return the storage capacity of the system
def storageCap(volume, distance, surfaceArea, innerDiameter, turbineOpeness):

    # Dump water
    dumpResults = dumpWater(volume, distance, surfaceArea, innerDiameter, turbineOpeness)

    # Energy Total
    dEnergy = dumpResults[8]
    
    # Net Energy

    return dEnergy


# Function to return the maximum power of the system
def maxPower(volume, distance, surfaceArea, innerDiameter, turbineOpeness):
    dumpResults = dumpWater(volume, distance, surfaceArea, innerDiameter, turbineOpeness)

    return max(dumpResults[9])


# Function to plot a heatmap of varying distance and volume against net energy using plotly
def plotHeatmap(pbounds,points):

    minVolume, maxVolume = pbounds['volume'][0], pbounds['volume'][1]
    minDistance, maxDistance = pbounds['distance'][0], pbounds['distance'][1]
    pumpPower = pbounds['pumpPower'][0]
    surfaceArea = pbounds['surfaceArea'][0]
    innerDiameter = pbounds['innerDiameter'][0]
    turbineOpeness = pbounds['turbineOpeness'][0]

    # Create a list of volumes
    volumeList = np.linspace(minVolume, maxVolume, points)

    # Create a list of distances
    distanceList = np.linspace(minDistance, maxDistance, points)

    # Create a list of net energy
    netEnergyList = np.zeros((len(volumeList), len(distanceList)))

    # Loop through the lists
    for i in range(len(volumeList)):
        for j in range(len(distanceList)):
            netEnergyList[j][i] = netEnergy(volumeList[i], distanceList[j], pumpPower, surfaceArea, innerDiameter, turbineOpeness)
            print("Plotting point: ", i+1, j+1, "of", len(volumeList), len(distanceList))

    # Create the heatmap
    fig = go.Figure(data=go.Heatmap(
        x=volumeList,
        y=distanceList,
        z=netEnergyList,
        colorscale='blugrn'))

    fig.update_layout(
        title='Net Energy of the System',
        xaxis_title='Volume (m^3)',
        yaxis_title='Distance (m)',
        xaxis_nticks=36,
    )

    fig.show()


# Function to Bayesian optimise the system
def bayesianOptimise(pbounds, initPoints, iterations):
    
    # Prefer exploration over exploitation
    acquisition_function = UtilityFunction(kind="poi", xi=1e-1)

    # Create the optimiser
    optimiser = BayesianOptimization(
        f=netEnergy,
        pbounds=pbounds,
        verbose=2,
        allow_duplicate_points=True
    )

    optimiser.maximize(
        init_points=initPoints,
        n_iter=iterations,
        acquisition_function=acquisition_function
    )

    print(optimiser.max)

    return(optimiser)

# maximumPower = maxPower(optimiser.max['params']['volume'], optimiser.max['params']['distance'], optimiser.max['params']['surfaceArea'], optimiser.max['params']['innerDiameter'], optimiser.max['params']['turbineOpeness'])
# print("The maximum power generated is: ", round(maximumPower, 2), "Watts /", round(maximumPower/1000, 2), "Kilowatts /", round(maximumPower/1000000, 2), "Megawatts")

def plotBayesian(optimiser):

    volumes = []
    distances = []
    nets = []

    res = optimiser.res
    for i in range(len(res)):
        volumes.append(res[i]['params']['volume'])
        distances.append(res[i]['params']['distance'])
        nets.append(res[i]['target'])

    print(volumes[0])

    fig = px.scatter(
        x=volumes, 
        y=distances, 
        color=nets, 
        color_continuous_scale="blugrn", 
        title="Bayesian Optimization Result", 
        labels={'color': 'Net Energy'},
    )

    fig.update_layout(
        xaxis_title="Volume of Water / m^3",
        yaxis_title="Distance Between Tanks / m",
    )

    fig.update_traces(
        marker_size=20,
        marker_line_width=2,
        marker_line_color='White',
    )

    # More ticks on the x-axis
    fig.update_xaxes(nticks=20)

    # More ticks on the y-axis
    fig.update_yaxes(nticks=20)

    fig.show()
