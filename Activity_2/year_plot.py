import matplotlib.pyplot as plt
import numpy as np

# Fixed parameters
dl = 12  # day length (hrs)
ea = 1   # saturation vapor pressure at daily temp
LAI_corn = 5.9
LAI_tree_plantation = 5.8
LAI_grass = 1.5

# Monthly precipitation values (inches/month) – replace with your location data
P_monthly_in = [0.69, 1.02, 2.01, 3.89, 4.99, 4.89, 
                4.53, 4.75, 3.47, 2.63, 1.86, 1.17]

# Monthly average daily temperatures (°F) – replace with local averages
T_monthly = [29, 34, 48, 62, 73, 81, 84, 82, 77, 64, 47, 34]

# Months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Store ET results
ET_crop_list = []
ET_grass_list = []
ET_forest_list = []

# Loop through each month with precipitation + temp
for P_in, T_f in zip(P_monthly_in, T_monthly):
    # Convert precip from inches to mm (1 in = 25.4 mm)
    P = P_in * 25.4  
    T = (T_f-32) * (5/9)
    # Monthly PET (depends on temp)
    PET_h = 29.8 * dl * (ea / (T + 273.2))
    
    # ET equations (mm)
    ET_crop = P -(-8.15) + (0.86 * PET_h) + (0.09 * P) + (9.54 * LAI_corn)
    ET_grass = P - (-1.36) + (0.70 * PET_h) + (0.01 * P) + (9.54 * LAI_grass)
    ET_forest_d = P - (-14.82) + (0.98 * PET_h) + (0.04 * P) + (6.56 * LAI_tree_plantation)
    
    ET_crop_list.append(ET_crop)
    ET_grass_list.append(ET_grass)
    ET_forest_list.append(ET_forest_d)

# Convert to numpy arrays
ET_crop_list = np.array(ET_crop_list)
ET_grass_list = np.array(ET_grass_list)
ET_forest_list = np.array(ET_forest_list)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(months, ET_crop_list, marker="o", label="Cropland", color="red")
plt.plot(months, ET_grass_list, marker="s", label="Grassland", color="gold")
plt.plot(months, ET_forest_list, marker="^", label="Deciduous Forest", color="forestgreen")

# Threshold line (90 mm ≈ 2 inches)
plt.axhline(18.0, color="blue", linestyle="--", label="Wilting Point (18.0 mm)")

plt.ylabel("Precipitation(mm) - Evapotranpiration (mm)")
plt.title("Monthly Evapotranspiration by Sandy Loam (20 cm depth)")
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

