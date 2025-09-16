'''
Author: Alex Cecil
email: ajcecil@iastate.edu
Date Created: 2025-09-14
Last Modified: 2025-09-14
Purpose: Produce plots for different plant systems and their evapotranspiration. 
'''


import matplotlib.pyplot as plt

# Given values
dl = 12  # day length (hrs)
ea = 1   # Saturation vapor pressure at daily temp
T = (84-32) * (5/9)  # daily temp in Celsius
P = (4.53 * 25.4)  # precipitation (mm/month)
LAI_corn = 5.9  # square meters/square meters
LAI_tree_plantation = 5.8
LAI_grass = 1.5

# Potential evapotranspiration
PET_h = 29.8 * dl * (ea / (T + 273.2))

# ET calculations
ET_crop = (-8.15) + (0.86 * PET_h) + (0.09 * P) + (9.54 * LAI_corn)
ET_grass = (-1.36) + (0.70 * PET_h) + (0.01 * P) + (9.54 * LAI_grass)
ET_forest_d = (-14.82) + (0.98 * PET_h) + (0.04 * P) + (6.56 * LAI_tree_plantation)

# Data for plotting
systems = ["Cropland", "Grassland", "Deciduous Forest"]
ET_values = [ET_crop, ET_grass, ET_forest_d]

# Plot
plt.figure(figsize=(8, 6))
plt.bar(systems, ET_values, color=["red", "gold", "forestgreen"], edgecolor="black")
plt.ylabel("ET (mm/month)")
plt.title("Evapotranspiration by System")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()
