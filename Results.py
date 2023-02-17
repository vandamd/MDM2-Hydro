from Results_Functions import *


# ----- Variables for Dumping & Pumping -----
dumpTime = "08:00"
pumpTime = "20:00"
volume = 1.542714
distance = 50
pumpPower = 3000
surfaceArea = 10
innerDiameter = 0.25
turbineOpeness = 100

# ----- Graph of Dumping Water -----
# plotDump(volume, distance, surfaceArea, innerDiameter, turbineOpeness)

# ----- Graph of Pumping Water -----
# plotPump(volume, distance, pumpPower, surfaceArea, innerDiameter)

# ----- Graph of a cycle with Net Energy (Dump then Pump) -----
# cycleWater(dumpTime, pumpTime, volume, distance, pumpPower, surfaceArea, innerDiameter, turbineOpeness)




# ----- Varibales for the Heatmap & Bayesian Optimisation -----
pbounds = {'volume': (1, 10), 'distance': (1, 50), 'pumpPower': (3000, 3000), 'surfaceArea': (10, 10), 'innerDiameter': (0.25, 0.25), 'turbineOpeness': (100, 100)}

# ----- Heatmap -----
plotHeatmap(pbounds, 100)

# ----- Bayesian Optimisation -----
# bayesianOptimise(pbounds, 100, 5)

# ----- Plot of the Bayesian Optimisation -----
# plotBayesian(bayesianOptimise(pbounds, 10000, 0))