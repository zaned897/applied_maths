"""In this code we will continue with the multiple variables functions

Lecture: explore characteristics in multiple variables functions
"""

#%%
import numpy as np
from matplotlib import pyplot as plt

# define the vector space
x = np.linspace(
	start=-3*np.pi,
	stop=3*np.pi,
	num=200
)
y = x
# create the mesh for the function evaluation
X, Y = np.meshgrid(x, y)

# evaluate the function on X and Y
Z = X*np.sin(Y) + Y*np.cos(X)

#%%
fig = plt.figure(figsize=(15, 7))

# 3D surface plot
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('3D Surface Plot')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.set_zlabel('Z-axis')
ax1.text2D(0.05, 0.95, r"$Z = X \cos(Y) + Y \sin(X)$", transform=ax1.transAxes)

# Contour plot
ax2 = fig.add_subplot(1, 2, 2)
contour = ax2.contourf(X, Y, Z)
ax2.set_title('Contour Plot')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
cbar = plt.colorbar(contour)
cbar.set_label('Z-axis')
ax2.text(0.05, 0.95, r"$Z = X \cos(Y) + Y \sin(X)$", transform=ax2.transAxes)

plt.show()