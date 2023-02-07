import numpy as np

# Tank Attributes
# initialTopDepth = 0                                         # ! Depth of the top tank
# initialBottomDepth = 0                                      # ! Depth of the bottom tank
# maximumDepth = 1
# minimumDepth = 0
# baseToBase = 10                                             # ! Distance between the bottom of each tank

# minimumVolume = 0                                           # Minimum Volume of each tank (can't be negative lol)
# maximumVolume = 1                                           # ! Maximum Volume of each tank 
surfaceArea = 1                                             # Surface area of each tank

# Pipe Attributes
# Length = baseToBase                                         # Length of the pipes 
innerD = 0.5                                                # Inner diameter of the pipes               
f = 0.01                                                    # Friction factor

# Pump Attributes
pumpEfficiency = 0.8                                        # Pump efficiency
# inputPower = 5                                               # Input power in watts

# Environment Attributes
g = 9.81                                                    # Gravity
timeSpan = 86400                                            # In seconds
t = np.linspace(0,timeSpan,timeSpan)                        # Time span in seconds (24 hours)
waterDensity = 997                                          # Density of water in kilograms per cubic meter
precip = 0                                                  # Precipitation rate in cubic meters per second
evap = 0                                                    # Evaporation rate in cubic meters per second