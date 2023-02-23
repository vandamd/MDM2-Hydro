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
# plotHeatmap(pbounds, 100)

# ----- Bayesian Optimisation -----
# bayesianOptimise(pbounds, 100, 100)

# ----- Bayesian Optimisation 2 -----
# distances = [100, 150, 200, 300, 500]
# # diameters = [0.1, 0.2, 0.5]
# diameters = [0.5]

# Bayesian Optimise for different distances and diameters
# for j in range(len(diameters)):
#     for i in range(len(distances)):
#         pbounds = {'volume': (0.02, 0.02), 'distance': (distances[i], distances[i]), 'pumpPower': (1, 15000), 'surfaceArea': (0.0784, 0.0784), 'innerDiameter': (diameters[j], diameters[j]), 'turbineOpeness': (100, 100)}
#         bayesianOptimise2(pbounds, 500, 50)
#         storageCap(0.02, distances[i], 0.0784, diameters[j], 100)

# ----- Plot of the Bayesian Optimisation -----
# plotBayesian(bayesianOptimise(pbounds, 500, 50))

height = [1.5, 5, 10, 20, 30, 50, 75, 100]
diameters = [100, 200, 500]

payback100 = [4290.97, 1444.93, 853.72, 538.64, 421.24, 314.22, 251.28, 215.19]
payback200 = [983.4, 353.4, 215.19, 139.03, 109.8, 82.7, 66.53, 57.19]
payback500 = [195.04, 82.62, 53.84, 36.35, 29.19, 22.31, 18.09, 15.61]

extraHeights = [100, 150, 200, 300, 500]
paybackExtra = [15.61, 12.7, 10.98, 8.95, 6.92]

# Plot two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# fig.suptitle('Payback Period vs Height Difference')

# Plot the payback100, payback200, payback500 on the left subplot
ax1.plot(height, payback100, label = "Diameter = 100m", color = "blue")
ax1.plot(height, payback200, label = "Diameter = 200m", color = "red")
ax1.plot(height, payback500, label = "Diameter = 500m", color = "green")
ax1.set_xlabel("Height Difference (m)")
ax1.set_ylabel("Payback Period (years)")

# Plot the paybackExtra on the right subplot
ax2.plot(extraHeights, paybackExtra, label = "Diameter = 500m, Extended", color = "orange")
# ax2.plot(height, payback100, label = "Diameter = 100m", color = "blue")
ax2.plot(height, payback200, label = "Diameter = 200m", color = "red")
ax2.plot(height, payback500, label = "Diameter = 500m", color = "green")
ax2.set_xlabel("Height Difference (m)")
ax2.set_ylabel("Payback Period (years)")
# Set limits between 100m to 500m
ax2.set_xlim(40, 500)
# Auto scale the y-axis to fit the data
ax2.set_ylim(0, 150)

# Show the legend and grid
ax1.legend()
ax1.grid()
ax2.legend()
ax2.grid()

# Show the plot
plt.show()