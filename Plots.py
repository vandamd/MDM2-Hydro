from Pump import *
from Dump import *
import pprint as pp

# ----- PUMPING & DUMPING WATER -----
depth = 1
volume = 1.2
distance = 13
pumpPower = 10
surfaceArea = 1
innerDiameter = 0.1
turbineOpeness = 0.2

# pumpResults = pumpWater(depth, volume, distance, pumpPower, surfaceArea, innerDiameter)
pumpResults = dumpWater(depth, volume, distance, surfaceArea, innerDiameter, turbineOpeness)
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

limit = 12000
# pp.pprint(topTankVolumes[-5:-1])dd
# pp.pprint(t)

# Define figure 
fig = plt.figure()

# Define figure with 5 subplots
subfigs = fig.subfigures(1, 5, wspace=0.7)

axsLeft = subfigs[0].subplots(1, 1)
axsLeft.plot(t, topTankVolumes, 'b', label='Top Tank')
axsLeft.plot(t, bottomTankVolumes, 'r', label='Bottom Tank')
axsLeft.legend(loc='best')
axsLeft.set_title('Volume of Water in the Top Tank')
axsLeft.set_xlabel('Time (s)')
axsLeft.set_ylabel('Volume (m^3)')
axsLeft.grid()
axsLeft.set_xlim(-5, limit)

axsMid1 = subfigs[1].subplots(1, 1)
axsMid1.plot(t, pumpRates)
axsMid1.set_title('Flowrate of Water')
axsMid1.set_xlabel('Time (s)')
axsMid1.set_ylabel('Flowrate (m^3/s)')
axsMid1.grid()
axsMid1.set_xlim(-5, limit)

axsMid2 = subfigs[2].subplots(1, 1)
axsMid2.plot(t, pumpHeads)
axsMid2.set_title('Head of Water')
axsMid2.set_xlabel('Time (s)')
axsMid2.set_ylabel('Head (m)')
axsMid2.grid()
axsMid2.set_xlim(-5, limit)

axsMid3 = subfigs[3].subplots(1, 1)
axsMid3.plot(t, topDepths)
axsMid3.set_title('Depth of Water in the Top Tank')
axsMid3.set_xlabel('Time (s)')
axsMid3.set_ylabel('Depth (m)')
axsMid3.grid()
axsMid3.set_xlim(-5, limit)

axsRight = subfigs[4].subplots(1, 1)
axsRight.plot(t, pumpVelocities)
axsRight.set_title('Velocity of Water')
axsRight.set_xlabel('Time (s)')
axsRight.set_ylabel('Velocity (m/s)')
axsRight.grid()
axsRight.set_xlim(-5, limit)

plt.show()
