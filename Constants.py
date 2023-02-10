import numpy as np

# Pipe Attributes
f = 0.01                                                    # Friction factor

# Pump Attributes
pumpEfficiency = 0.8                                        # Pump efficiency

# Turbin Attributes
turbineEfficiency = 0.8                                     # Turbine efficiency

# Environment Attributes
g = 9.81                                                    # Gravity
timeSpan = 86400                                            # In seconds
t = np.linspace(0,timeSpan,timeSpan)                        # Time span in seconds (24 hours)
waterDensity = 997                                          # Density of water in kilograms per cubic meter