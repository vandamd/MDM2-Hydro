from Functions import *
import pprint as pp

# ----- PUMPING WATER -----
pumpResults = pumpWater()
pumpHeads = pumpResults[0]
pumpRates = pumpResults[1]
pumpVelocities = pumpResults[2]
pumpVelocities = pumpVelocities[:-1]
topTankVolumes = pumpResults[3]
bottomTankVolumes = pumpResults[4]

# pp.pprint(pumpRates[:5])
# pp.pprint(t)

# Define figure 
fig = plt.figure()

# Define figure with 2 subplots
subfigs = fig.subfigures(1, 4, wspace=0.7)

axsLeft = subfigs[0].subplots(1, 1)
axsLeft.plot(t, topTankVolumes, 'b', label='Top Tank')
axsLeft.plot(t, bottomTankVolumes, 'r', label='Bottom Tank')
axsLeft.legend(loc='best')
axsLeft.set_title('Volume of Water in the Top Tank')
axsLeft.set_xlabel('Time (s)')
axsLeft.set_ylabel('Volume (m^3)')
axsLeft.grid()
# axsLeft.set_xlim(-5, 50)

axsMid1 = subfigs[1].subplots(1, 1)
axsMid1.plot(t, pumpRates)
axsMid1.set_title('Flowrate of Water')
axsMid1.set_xlabel('Time (s)')
axsMid1.set_ylabel('Flowrate (m^3/s)')
axsMid1.grid()
# axsMid.set_xlim(-5, 50)

axsMid2 = subfigs[2].subplots(1, 1)
axsMid2.plot(t, pumpHeads)
axsMid2.set_title('Head of Water')
axsMid2.set_xlabel('Time (s)')
axsMid2.set_ylabel('Head (m)')
axsMid2.grid()
# axsMid.set_xlim(-5, 50)

axsRight = subfigs[3].subplots(1, 1)
axsRight.plot(t, pumpVelocities)
axsRight.set_title('Velocity of Water')
axsRight.set_xlabel('Time (s)')
axsRight.set_ylabel('Velocity (m/s)')
axsRight.grid()
# axsRight.set_xlim(-5, 50)

plt.show()
