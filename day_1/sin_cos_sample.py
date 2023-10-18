"""In this code we will explore a function $f(x,y) = xsin(y) + ycos(x)$"""
<<<<<<< HEAD
#%%
from numpy import cos, sin, pi, linspace, meshgrid
from matplotlib import pyplot as plt

# create the space
=======
from numpy import cos, sin, pi, linspace, meshgrid
from matplotlib import pyplot as plt

>>>>>>> ba93dd31411a2965437ded17cfd3efd3d0e206e1
x = linspace(
	start=-2*pi,
	stop=2*pi,
	num=200
)
y = x
<<<<<<< HEAD
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
=======
x, y = meshgrid
>>>>>>> ba93dd31411a2965437ded17cfd3efd3d0e206e1
