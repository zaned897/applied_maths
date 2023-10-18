"""In this code we will explore a function $f(x,y) = xsin(y) + ycos(x)$"""
#%%
from numpy import cos, sin, pi, linspace, meshgrid
from matplotlib import pyplot as plt

# create the space
from numpy import cos, sin, pi, linspace, meshgrid
from matplotlib import pyplot as plt

x = linspace(
	start=-2*pi,
	stop=2*pi,
	num=200
)
y = x
X, Y = meshgrid(x, y)

# Define the function
Z = X*sin(Y) + Y*cos(X)

#%% Results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('$g(x,y)=x\sin(y) + y\cos(x)$')
plt.show()
