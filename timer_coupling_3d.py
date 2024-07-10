import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the CSV file
csv_file = 'timer_coupling.csv'
df = pd.read_csv(csv_file)

# Separate the data into valid and missing z (steps) values
valid_data = df[df['steps'] != 0]
missing_data = df[df['steps'] == 0]

# Extract columns for valid data
x_valid = valid_data['coupling']
y_valid = valid_data['timer_offset']
z_valid = valid_data['steps']

# Extract columns for missing data
x_missing = missing_data['coupling']
y_missing = missing_data['timer_offset']

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the valid data
sc = ax.scatter(x_valid, y_valid, np.log(z_valid), c=np.log(z_valid), cmap='viridis', marker='o', depthshade=0, s=100)

# Plot the missing data points at log z = 8
log_z_missing = 8
ax.scatter(x_missing, y_missing, log_z_missing, c='r', marker='o', label='Simulation Divergiert', depthshade=0, s=100)

# Set labels
ax.set_xlabel('Kopplungsstärke')
ax.set_ylabel('Timer Variation')
ax.set_zlabel('Simulationsschritte bis zur Konvergenz (logaritmisch)')

# Add legend
ax.legend()

# Show the plot
plt.show()
