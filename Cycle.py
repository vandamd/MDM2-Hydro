from Pump import *
from Dump import *
import matplotlib.pyplot as plt

# User input times
# pumpTime = input("What time do you want to pump the water? (HH:MM)")
# dumpTime = input("What time do you want to dump the water? (HH:MM)")

# Variables
volume = 0.145
distance = 50
pumpPower = 5
surfaceArea = 1.5
innerDiameter = 0.1
turbineOpeness = 0.8

# Function to dump water then pump water at specific times in the day
def cycleWater(dumpTime, pumpTime, volume, distance, pumpPower, surfaceArea, innerDiameter, turbineOpeness):
    # # Convert time to seconds
    pumpTime = int(pumpTime[0:2]) * 3600 + int(pumpTime[3:5]) * 60
    dumpTime = int(dumpTime[0:2]) * 3600 + int(dumpTime[3:5]) * 60

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
    subfigs = fig.subfigures(3, 1)    
    
    axsTop = subfigs[0].subplots(1, 1)
    axsMid = subfigs[1].subplots(1, 1)
    axsBottom = subfigs[2].subplots(1, 1)

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

    # print(lossEnergy)

cycleWater("01:00", "20:00", volume, distance, pumpPower, surfaceArea, innerDiameter, turbineOpeness)
