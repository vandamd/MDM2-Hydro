from Results_Functions import *
import plotly.io as pio


# ----- Variables for Dumping & Pumping -----
dumpTime = "08:00"
pumpTime = "10:00"
volume = 0.02
distance = 100
pumpPower = 5586.7098373790695
surfaceArea = 0.0784
innerDiameter = 0.5
turbineOpeness = 100

# ----- Graph of Dumping Water -----
# plotDump(volume, distance, surfaceArea, innerDiameter, turbineOpeness)

# ----- Graph of Pumping Water -----
# plotPump(volume, distance, pumpPower, surfaceArea, innerDiameter)

# ----- Graph of a cycle with Net Energy (Dump then Pump) -----
# cycleWater(dumpTime, pumpTime, volume, distance, pumpPower, surfaceArea, innerDiameter, turbineOpeness)




# ----- Variables for the Heatmap & Bayesian Optimisation -----
pbounds = {'volume': (0, 1), 'distance': (1.5, 100), 'pumpPower': (7500, 7500), 'surfaceArea': (0.257, 0.257), 'innerDiameter': (0.2, 0.2), 'turbineOpeness': (100, 100)}
# pbounds = {'volume': (0.02, 0.02), 'distance': (100, 100), 'pumpPower': (1, 15000), 'surfaceArea': (0.0784, 0.0784), 'innerDiameter': (0.5, 0.5), 'turbineOpeness': (100, 100)}

# ----- Heatmap -----
plotHeatmap(pbounds, 100)

# ----- Bayesian Optimisation -----
# bayesianOptimise(pbounds, 100, 100)

# ----- Bayesian Optimisation 2 -----
# distances = [100, 150, 200, 300, 500]
# diameters = [0.1, 0.2, 0.5]
# diameters = [0.5]

# for j in range(len(diameters)):
#     for i in range(len(distances)):
#         pbounds = {'volume': (0.02, 0.02), 'distance': (distances[i], distances[i]), 'pumpPower': (1, 15000), 'surfaceArea': (0.0784, 0.0784), 'innerDiameter': (diameters[j], diameters[j]), 'turbineOpeness': (100, 100)}
#         bayesianOptimise2(pbounds, 500, 50)
#         # storageCap(0.02, distances[i], 0.0784, diameters[j], 100)

# ----- Plot of the Bayesian Optimisation -----
# plotBayesian(bayesianOptimise(pbounds, 500, 50))